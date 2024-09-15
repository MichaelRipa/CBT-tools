import os
import time
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from config import client_secrets_path, cloud_folder_id, data_dir, queue_file, processed_file, repo_path

# Authenticate with Google Drive
gauth = GoogleAuth()
gauth.LoadClientConfigFile(client_secrets_path)

# Try to load saved credentials, otherwise use web authentication
gauth.LoadCredentialsFile("credentials.json")

if gauth.credentials is None:
    # Authenticate if credentials are not available or expired
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline', 'prompt': 'consent'})
    gauth.LocalWebserverAuth()  # Creates local web server and auto-handles authentication
    # Save credentials for the next run
    gauth.SaveCredentialsFile("credentials.json")
elif gauth.access_token_expired:
    # Refresh credentials if the token is expired
    gauth.Refresh()
else:
    # Initialize the saved credentials
    gauth.Authorize()

drive = GoogleDrive(gauth)

# List of local files and their corresponding cloud file names
file_list = [
    {'local_path': os.path.join(repo_path, data_dir, queue_file), 'cloud_name': queue_file},
    {'local_path': os.path.join(repo_path, data_dir, processed_file), 'cloud_name': processed_file},
]

def get_drive_file(drive, cloud_file_name):
    # Search for the file by name on Google Drive
    file_list = drive.ListFile({'q': f"title='{cloud_file_name}'"}).GetList()
    if file_list:
        return file_list[0]  # Return the first matching file
    return None

def check_for_update(local_file_path, cloud_file_name):
    # Get local file modification time
    if not os.path.exists(local_file_path):
        print(f"Local file {local_file_path} does not exist!")
        return

    local_mod_time = os.path.getmtime(local_file_path)

    # Search for the file on Google Drive
    cloud_file = get_drive_file(drive, cloud_file_name)

    if cloud_file:
        # Get cloud file modification time
        cloud_mod_time = time.mktime(time.strptime(cloud_file['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ'))

        # Compare modification times
        if local_mod_time > cloud_mod_time:
            print(f"Local file {local_file_path} is newer. Uploading to Google Drive...")
            upload_to_drive(local_file_path, cloud_file, cloud_folder_id)
        else:
            print(f"Cloud file {cloud_file_name} is newer. Downloading to local system...")
            download_from_drive(local_file_path, cloud_file)
    else:
        # No file exists in the cloud, upload the local one
        print(f"File {cloud_file_name} does not exist on Google Drive. Uploading...")
        upload_to_drive(local_file_path, folder_id=cloud_folder_id)

def upload_to_drive(local_file_path, cloud_file=None, folder_id=None):
    cloud_file_name = os.path.basename(local_file_path)

    if cloud_file:
        # Update the existing cloud file
        cloud_file.SetContentFile(local_file_path)
        cloud_file.Upload()
        print(f'File "{cloud_file_name}" updated on Google Drive.')
    else:
        # Create a new file in the specified folder
        new_file_metadata = {'title': cloud_file_name}
        if folder_id:
            new_file_metadata['parents'] = [{'id': folder_id}]

        new_file = drive.CreateFile(new_file_metadata)
        new_file.SetContentFile(local_file_path)
        new_file.Upload()
        print(f'File "{cloud_file_name}" uploaded to Google Drive in folder ID "{folder_id}".')

def download_from_drive(local_file_path, cloud_file):
    # Download the file from Google Drive to local system
    cloud_file.GetContentFile(local_file_path)
    print(f'File "{local_file_path}" downloaded from Google Drive.')

if __name__ == "__main__":
    for file_info in file_list:
        local_file_path = file_info['local_path']
        cloud_file_name = file_info['cloud_name']
        check_for_update(local_file_path, cloud_file_name)


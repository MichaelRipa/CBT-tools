#! /usr/bin/python3

import os

repo_path = os.path.dirname(os.path.abspath(__file__))
data_dir = 'data'
cloud_folder_id = '' # Add the id of the gdrive directory you are backing up your results to
queue_file = 'rumination_queue.json'
processed_file = 'processed_ruminations.json'
client_secrets_path = os.path.join(repo_path, 'oauth', 'client_secrets.json')

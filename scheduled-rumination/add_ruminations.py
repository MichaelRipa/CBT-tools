#! /usr/bin/python3

from config import repo_path, queue_file

import json
from datetime import datetime
import os

def load_existing_ruminations(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

def main():
    # Ensure data directory exists
    data_dir = os.path.join(repo_path,'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    queue_file_path = os.path.join(data_dir, queue_file)
    ruminations = load_existing_ruminations(queue_file_path)

    while True:
        rumination = input("Enter what you are ruminating on: ")
        negativity_rating = int(input("Rate the negativity (0-9, where 9 is most negative): "))
        
        print("Choose an option:")
        print("1. Save result and continue")
        print("2. Save result and quit")
        print("3. Don't save result and continue")
        print("4. Don't save result and quit")
        choice = int(input("Enter your choice (1-4): "))
        
        if choice in [1, 2]:
            ruminations.append({
                'rumination': rumination, 
                'negativity_rating': negativity_rating, 
                'timestamp': datetime.now().isoformat()
            })
        
        if choice in [2, 4]:
            break

    if ruminations:  # Save regardless of the user's input to ensure no data is lost
        with open(queue_file_path, 'w') as f:
            json.dump(ruminations, f, indent=4)
        print("Results saved.")

if __name__ == "__main__":
    main()

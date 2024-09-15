#! /usr/bin/python3

from config import questions, json_path, json_file
from datetime import datetime
import json
import logging
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_results(results: dict) -> None:
    db_path = os.path.join(json_path, json_file)

    # Ensure the directory exists
    if not os.path.exists(json_path):
        logging.info(f'Creating directory at {json_path}')
        os.makedirs(json_path)

    # Initialize or load existing database
    if not os.path.isfile(db_path):
        logging.info(f'Creating gratitude journal db at {db_path}')
        current_db = {}
    else:
        with open(db_path, 'r') as file:
            current_db = json.load(file)

    today = datetime.today().strftime('%Y-%m-%d')
    if today in current_db:
        print(f'An entry for {today} already exists.')
        overwrite = input('Do you want to overwrite it? (yes/no): ')
        if overwrite.lower() != 'yes':
            print('Changes not saved. Exiting...')
            sys.exit()

    current_db[today] = results

    # Save the updated database
    with open(db_path, 'w') as file:
        json.dump(current_db, file, indent=4)
    logging.info(f'Data for {today} saved successfully.')

def gratitude_practice() -> dict:
    results = {}
    for q in questions:
        os.system('clear')  # Clear the console for better readability
        print(q)
        response = input('Your response: ')
        confirm = input('\nIs this your final response? (yes/no): ')
        if confirm.lower() == 'yes':
            results[q] = response
        print('\n\n')  # Additional spacing after each question
    return results

if __name__ == '__main__':
    results = gratitude_practice()
    save_confirm = input('Do you want to save your responses? (yes/no): ')
    if save_confirm.lower() == 'yes':
        write_results(results)
    else:
        print('Responses not saved. Exiting...')


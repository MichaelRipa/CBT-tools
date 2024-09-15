#!/usr/bin/python3

import json
from datetime import datetime
import os

from config import data_path, pre_exposure_file, post_exposure_file

# Utility function to confirm input with user
def confirm_input(prompt):
    while True:
        response = input(prompt)
        confirm = input(f"You entered '{response}'. Is this correct? (yes/no): ")
        if confirm.lower() == 'yes':
            return response

# Load data from JSON file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Load pre-exposure log and post-exposure log
def load_experiment_data():
    pre_log_path = os.path.join(data_path, pre_exposure_file)
    post_log_path = os.path.join(data_path, post_exposure_file)

    pre_exposure_logs = load_json_file(pre_log_path)
    post_exposure_logs = load_json_file(post_log_path)

    # Get the IDs of already completed exposures from the post-exposure logs
    completed_exposure_ids = [log['id'] for log in post_exposure_logs]

    # Filter out completed exposures by checking if the `id` is missing from post logs
    uncompleted_exposures = [
        log for log in pre_exposure_logs if log['id'] not in completed_exposure_ids
    ]

    # Sort by date (most recent first) and limit to the 15 most recent
    recent_uncompleted_exposures = sorted(
        uncompleted_exposures, key=lambda x: x['date'], reverse=True
    )[:15]

    return recent_uncompleted_exposures, post_exposure_logs

# Post-exposure follow-up log questions
def post_exposure_log(experiment):
    print(f"\nPost-exposure log for the experiment on {experiment['date']}:")
    ending_suds = int(confirm_input("Ending SUDS (0-100): "))
    
    worry_came_true = confirm_input("Did your worry/negative belief come true? (Y/N): ").lower()
    evidence = ""
    if worry_came_true == 'n':
        evidence = confirm_input("What evidence do you have that it didn’t come true? ")

    belief_now = int(confirm_input("How much do you believe your original worry/negative thought now? (0-100%): "))
    
    new_learning = confirm_input("How would you change your belief to account for the new learning? ")
    
    new_belief = {}
    new_belief_text = confirm_input("Enter the new thought(s): ")
    new_belief_strength = int(confirm_input(f"How much do you believe this new thought '{new_belief_text}'? (0-100%): "))
    new_belief[new_belief_text] = new_belief_strength

    return {
        'id': experiment['id'],  # Include the `id` for tracking
        'date': experiment['date'],
        'ending_suds': ending_suds,
        'worry_came_true': worry_came_true,
        'evidence': evidence,
        'belief_now': belief_now,
        'new_learning': new_learning,
        'new_belief': new_belief
    }

# Save post-exposure log to JSON
def save_post_exposure_log(post_logs, new_log):
    post_log_path = os.path.join(data_path, post_exposure_file)

    post_logs.append(new_log)

    with open(post_log_path, 'w') as file:
        json.dump(post_logs, file, indent=4)

    print("Post-exposure log saved successfully.")

def main():
    # Load experiment data
    recent_exposures, post_exposure_logs = load_experiment_data()

    if not recent_exposures:
        print("No recent uncompleted exposures found.")
        return

    # Display the available recent uncompleted exposures
    print("\nRecent uncompleted exposures:")
    for idx, exposure in enumerate(recent_exposures):
        print(f"{idx + 1}. ID: {exposure['id']} | Activity: {exposure['activity']} | Date: {exposure['date']}")

    # Let the user select which experiment to log a follow-up for by `id`
    selected_id = int(confirm_input("\nEnter the ID of the experiment to log follow-up for: "))

    # Find the selected experiment by ID
    selected_experiment = next((exp for exp in recent_exposures if exp['id'] == selected_id), None)

    if selected_experiment:
        post_log_entry = post_exposure_log(selected_experiment)
        save_post_exposure_log(post_exposure_logs, post_log_entry)
    else:
        print("Invalid ID. Exiting.")

if __name__ == "__main__":
    main()

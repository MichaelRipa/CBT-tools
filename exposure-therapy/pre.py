#!/usr/bin/python3

import json
from datetime import datetime
import os

from config import data_path, pre_exposure_file, post_exposure_file

def confirm_input(prompt):
    while True:
        response = input(prompt)
        if response.lower() == 'done':
            return response
        confirm = input(f"You entered '{response}'. Is this correct? (yes/no): ")
        if confirm.lower() == 'yes':
            return response

def log_experiment():
    print("Pre-exposure/experiment log")

    # Activity Details
    activity = confirm_input("What are you going to do for your exposure/experiment? (e.g., Make small talk with a coworker about their weekend for 5 minutes): ")
    when = confirm_input("When are you planning to do it? (e.g., Tuesday before team meeting): ")
    what = confirm_input("What specifically will you do? (e.g., Go to the office kitchen and ask someone what they did over the weekend): ")
    duration = confirm_input("How long will it last? (e.g., 5 minutes): ")

    # Obstacles and Solutions
    print("\nWhat might get in the way of your exposure/experiment?")
    obstacle = confirm_input("Obstacle 1: ")
    solution = confirm_input(f"What will you do if '{obstacle}' arises?: ")

    more_obstacles = input("Do you have more obstacles to consider? (yes/no): ").lower()
    obstacles = {obstacle: solution}
    while more_obstacles == "yes":
        obstacle = confirm_input("Enter another obstacle: ")
        solution = confirm_input(f"What will you do if '{obstacle}' arises?: ")
        obstacles[obstacle] = solution
        more_obstacles = input("Do you have more obstacles to consider? (yes/no): ").lower()

    # SUDS
    suds = int(confirm_input("Starting SUDS (0-100): "))

    # Worries and Negative Beliefs
    worry = confirm_input("What do you worry is going to happen? (e.g., awkward pause, freeze up): ")
    belief_level = int(confirm_input("How likely do you feel this negative outcome is (0-100)?: "))

    # Record the experiment log
    record = {
        'date': datetime.now().isoformat(),
        'activity': activity,
        'when': when,
        'what': what,
        'duration': duration,
        'obstacles': obstacles,
        'suds': suds,
        'worry': worry,
        'belief_level': belief_level
    }

    # Save to JSON file
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    file_path = os.path.join(data_path, pre_exposure_file)

    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    record['id'] = len(existing_data) + 1
    existing_data.append(record)

    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("Experiment log saved. You can review it later or add more entries.")
    return record

def main():
    log_experiment()


if __name__ == "__main__":
    main()


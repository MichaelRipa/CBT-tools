#!/usr/bin/python3

import json
from datetime import datetime
import os
import sys

def get_input(prompt):
    print(prompt)
    entries = []
    while True:
        entry = input()
        if entry.lower() == 'done':
            break
        entries.append(entry)
    return entries

def process_thought(thought):
    responses = {
        'date': datetime.now().isoformat(),
        'thought': thought,
        'what_is_bothering_you': get_input("What's bothering you about the thought? (Type 'done' when finished):"),
        'reality_to_accept': get_input("Is there something here that is a reality you have to accept (vs a judgement or opinion)? (Type 'done' when finished):"),
        'thoughts_for_acceptance': get_input("Can you accept this reality in your thoughts? What can you tell yourself to help you accept this reality? (Type 'done' when finished):"),
        'behavior_changes_if_accepted': get_input("Imagine how you'd change your behaviors or actions if you accepted this reality? (Type 'done' when finished):"),
        'physical_acceptance': get_input("Can you accept it in your body? Where are you carrying the resistance? (Type 'done' when finished):"),
        'emotions_felt': get_input("Do you feel disappointment, sadness, or grief right now? (Type 'done' when finished):"),
        'life_worth_living': get_input("Despite the pain of this reality, what makes life worth living? (Type 'done' when finished):"),
        'pros_and_cons': get_input("Write down some pros and cons of accepting or not accepting this reality. (Type 'done' when finished):")
    }

    # Save to JSON file
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    file_path = os.path.join(data_dir, 'radical_acceptance_records.json')

    existing_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

    existing_data.append(responses)

    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("Radical acceptance record saved. You can review it later or add more entries.")
    return responses

def main():
    # Check if a thought is provided via command line argument
    if len(sys.argv) > 1:
        # If called as a subprocess, expect a JSON string
        try:
            input_data = json.loads(sys.argv[1])
            thought = input_data['rumination']
        except (json.JSONDecodeError, KeyError):
            thought = sys.argv[1]  # Fallback to treating the argument as a plain string
    else:
        # If not, ask the user to enter a thought
        thought = get_input("Enter your current thought or rumination:")
        thought = thought[0] if thought else ""  # get_input returns a list, so we take the first element

    result = process_thought(thought)

    # If called as a subprocess, print the result as JSON
    if len(sys.argv) > 1:
        print(json.dumps(result))

if __name__ == "__main__":
    main()

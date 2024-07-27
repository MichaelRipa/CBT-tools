#!/usr/bin/python3

import json
from datetime import datetime
import sys
import os

def get_input(prompt):
    result = input(prompt)
    return result

def process_thought(thought):
    print("\n--- Cognitive Defusion Exercise ---")
    print(f"I'm noticing that I'm having the thought that {thought}")

    # Explore the function of the thought
    function = get_input("What is the function of this thought? What is it alerting you to? (Type your response):")
    themes = get_input("Name your mind's favorite themes or 'signature moves' that relate to this thought (Type your response):")
    helpfulness = get_input("Is this thought a helpful guide? (yes/no):")
    if helpfulness.lower() == 'yes':
        action_taken = get_input("What wise action does this thought suggest? (Type your response):")
        alternative_action = None
    else:
        action_taken = None
        alternative_action = get_input("What would you be doing if this thought didn't take control? How would you like to respond? (Type your response):")

    defusion_record = {
        'date': datetime.now().isoformat(),
        'thought': thought,
        'function': function,
        'themes': themes,
        'helpfulness': helpfulness,
        'action_taken': action_taken,
        'alternative_action': alternative_action
    }

    # Save to JSON file
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    file_path = os.path.join(data_dir, 'cognitive_defusion_records.json')

    existing_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

    existing_data.append(defusion_record)

    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("\nCognitive defusion exercise completed and saved. You can review it later or add more entries.")
    return defusion_record

def main():
    if len(sys.argv) > 1:
        try:
            input_data = json.loads(sys.argv[1])
            thought = input_data['rumination']
        except (json.JSONDecodeError, KeyError):
            thought = sys.argv[1]
    else:
        thought = get_input("Enter your current thought or rumination:")

    result = process_thought(thought)

    if len(sys.argv) > 1:
        print(json.dumps(result))

if __name__ == "__main__":
    main()

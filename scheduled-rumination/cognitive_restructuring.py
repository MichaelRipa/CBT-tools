#!/usr/bin/python3

import json
from datetime import datetime
import os
import sys

def confirm_input(prompt):
    while True:
        response = input(prompt)
        if response == 'done':
            return response
        confirm = input(f"You entered '{response}'. Is this correct? (yes/no): ")
        if confirm.lower() == 'yes':
            return response

def get_multiple_entries(prompt, followup_prompt = None):
    entries = [] if followup_prompt is None else {}
    print(prompt)
    while True:
        item = confirm_input("Enter an item or type 'done' to finish:\n")
        if item.lower() == 'done':
            break
        if followup_prompt is not None:
            followup = int(confirm_input(followup_prompt.format(item)))
            entries[item] = followup
        else:
            entries.append(item)
    return entries

def probing_questions(chosen_thought):
    questions = [
        "1. What is the effect of believing this thought? What would happen if you didn't believe this thought?",
        "2. What is the evidence supporting this thought? What is the evidence against this thought?",
        "3. Is there an alternative explanation?",
        "4. What's the worst that could happen, and would I survive it? What's the best that could happen? What is the most likely scenario?",
        "5. If my friend were in this situation, what would I tell them?",
        "6. What can I do about this?"
    ]
    responses = {}
    print(f"\nProbing Questions for the thought: '{chosen_thought}'")
    for question in questions:
        response = confirm_input(question + " ")
        responses[question] = response
    return responses

def process_thought(initial_thought):
    situation = get_multiple_entries("\nSITUATION\nWhat event(s) led to the negative emotions?\n")
    emotions = get_multiple_entries("\nEMOTIONS\nWhat emotion(s) did you feel?", "Rate the intensity of '{}' (0-100):\n")
    automatic_thoughts = get_multiple_entries("\nAUTOMATIC THOUGHTS\nWhat thoughts/images ran through your mind?\n", "How strongly do you believe '{}'? (0-100): ")
    print("\nAvailable Automatic Thoughts:")
    for thought, belief in automatic_thoughts.items():
        print(f"'{thought}' - Belief level: {belief}")
    
    chosen_thought = confirm_input("Choose an automatic thought to analyze further:")
    responses = probing_questions(chosen_thought)
    alternative_response = confirm_input("Now, based on your responses, formulate an alternative response:")

    record = {
        'date': datetime.now().isoformat(),
        'initial_thought': initial_thought,
        'situation': situation,
        'emotions': emotions,
        'automatic_thoughts': automatic_thoughts,
        'chosen_thought': chosen_thought,
        'probing_questions_responses': responses,
        'alternative_response': alternative_response
    }

    # Save to JSON file
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    file_path = os.path.join(data_dir, 'cognitive-restructuring.json')

    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(record)

    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

    print("Cognitive restructuring record saved. You can review it later or add more entries.")
    return record

def main():
    if len(sys.argv) > 1:
        try:
            input_data = json.loads(sys.argv[1])
            initial_thought = input_data['rumination']
        except (json.JSONDecodeError, KeyError):
            initial_thought = sys.argv[1]
    else:
        initial_thought = confirm_input("Enter your current thought or rumination:\n")

    result = process_thought(initial_thought)

    if len(sys.argv) > 1:
        print(json.dumps(result))

if __name__ == "__main__":
    main()

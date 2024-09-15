#!/usr/bin/python3

import json
import os
from config import queue_file, processed_file, repo_path
from cognitive_defusion import process_thought as cognitive_defusion
from cognitive_restructuring import process_thought as cognitive_restructuring
from radical_acceptance import process_thought as radical_acceptance

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def confirm(prompt):
    while True:
        response = input(f"\n{prompt} (yes/no): ").lower()
        print()  # Add a newline after the response
        if response in ['yes', 'no']:
            return response == 'yes'

def get_negativity_rating():
    while True:
        try:
            negativity_rating = int(input("Rate the negativity after reflecting (0-9, where 9 is most negative): "))
            assert 0 <= negativity_rating and 9 >= negativity_rating
            break
        except:
            pass

    return negativity_rating


def main():
    queue_path = os.path.join(repo_path, 'data', queue_file)
    processed_path = os.path.join(repo_path, 'data', processed_file)
    
    ruminations = load_data(queue_path)
    processed_ruminations = load_data(processed_path)

    ruminations.sort(key=lambda x: -x['negativity_rating'])

    for rumination in ruminations:
        print(f"\n{'='*50}\nReviewing rumination: {rumination['rumination']}\n{'='*50}\n")

        processed_entry = {
            'rumination': rumination,
            'steps': [],
            'result': None
        }

        if not confirm("Is this thought or rumination relevant to your current situation?"):
            processed_entry['result'] = 'not relevant'
            negativity_rating = get_negativity_rating()
            processed_entry["post_rating"] = negativity_rating
            processed_ruminations.append(processed_entry)
            ruminations.remove(rumination)
            save_data(ruminations, queue_path)
            save_data(processed_ruminations, processed_path)
            if not confirm("Would you like to proceed to the next queued thought?"):
                break
            continue

        processed_entry['steps'].append('relevant')

        if not confirm("Do you believe this thought or rumination is factually true?"):
            processed_entry['result'] = 'not true'
            processed_entry['steps'].append('not true')
            if confirm("Is this thought still bothering you or getting in your way?"):
                diffusion_result = cognitive_defusion(rumination['rumination'])
                processed_entry['cognitive_defusion'] = diffusion_result

            negativity_rating = get_negativity_rating()
            processed_entry["post_rating"] = negativity_rating
            processed_ruminations.append(processed_entry)
            ruminations.remove(rumination)
            save_data(ruminations, queue_path)
            save_data(processed_ruminations, processed_path)
            if not confirm("Would you like to proceed to the next queued thought?"):
                break
            continue
        
        processed_entry['steps'].append('potentially true')

        if not confirm("Is this an indisputable fact, rather than an opinion or something you're uncertain about?"):
            if confirm("Would you like to try cognitive restructuring to examine this thought more closely?"):
                restructuring_result = cognitive_restructuring(rumination['rumination'])
                processed_entry['cognitive_restructuring'] = restructuring_result
            elif confirm("Would you prefer to revisit this thought later?"):
                continue  # Keep it in the queue
            else:
                processed_entry['result'] = 'accepted without restructuring'
        else:
            processed_entry['steps'].append('indisputable fact')
            if confirm("Is there something you can do about this situation?"):
                first_step = input("\nWhat would be a good first step to start addressing this?\n")
                processed_entry['action_step'] = first_step
                print("\nConsider applying Mental Contrasting with Implementation Intentions (MCII) to plan your approach.")
            elif confirm("Would you like to practice radical acceptance for this situation?"):
                acceptance_result = radical_acceptance(rumination['rumination'])
                processed_entry['radical_acceptance'] = acceptance_result

        if confirm("Is this thought still bothering you or getting in your way?"):
            diffusion_result = cognitive_defusion(rumination['rumination'])
            processed_entry['cognitive_defusion'] = diffusion_result

        # See how salient thought is after reflection
        negativity_rating = get_negativity_rating()
        processed_entry["post_rating"] = negativity_rating

        ruminations.remove(rumination)
        processed_ruminations.append(processed_entry)

        save_data(ruminations, queue_path)
        save_data(processed_ruminations, processed_path)

        if not confirm("Would you like to proceed to the next queued thought?"):
            break

        print("\n" + "="*50 + "\n")  # Add a separator between ruminations

if __name__ == "__main__":
    main()

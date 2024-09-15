#! /usr/bin/python3

import os

questions = [
        'What challanges did I face today and what did I learn from them?',
        'What are 3 to 5 things that I am grateful for today?',
        'Who made a positive difference in your day?'
]

file_path = os.path.dirname(os.path.abspath(__file__))

# Path to the directory where you want the results written to
json_path = os.path.join(file_path, 'data')

# Name of the json file which results are written to
json_file = 'graditude.json'

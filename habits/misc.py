#! /usr/bin/python3

import random
import argparse

def intentional_imperfection():
    behavior = input("Enter the behavior you want to perform inconsistently: ")
    days_per_week = int(input("How many days per week do you want to perform this behavior? (e.g., 5): "))
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    random.shuffle(days)
    
    print(f"Plan to perform {behavior} on the following days:")
    for day in days[:days_per_week]:
        print(f"- {day}")

def micro_habits():
    goal = input("Enter your ultimate goal (e.g., start running): ")
    steps = []
    
    print("Enter the smallest possible actions that could lead to your goal, one at a time.")
    print("When you are done, type 'done'.")
    
    while True:
        step = input("Enter a small step: ")
        if step.lower() == 'done':
            break
        steps.append(step)
    
    print(f"To achieve your goal of {goal}, start with the following steps:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

def intrinsic_motivation():
    goal = input("Enter the habit you want to develop: ")
    enjoyable_versions = []
    
    print(f"Think of versions of {goal} that are enjoyable or intriguing to you.")
    print("Enter them one by one. When you are done, type 'done'.")
    
    while True:
        version = input("Enter an enjoyable version: ")
        if version.lower() == 'done':
            break
        enjoyable_versions.append(version)
    
    print(f"Here are some enjoyable versions of {goal} you can try:")
    for version in enjoyable_versions:
        print(f"- {version}")

def positive_reinforcement():
    behavior = input("Enter the behavior you want to reinforce: ")
    reward = input("Enter a reward you can give yourself (e.g., draw a star, tell a friend): ")
    
    print(f"Whenever you perform {behavior}, even if not perfectly, remember to {reward}.")

def environment_change():
    goal = input("Enter the behavior you want to change (e.g., hydrate more): ")
    environment_tips = input(f"Enter ways to change your environment to support {goal} (e.g., keep full water bottles in multiple locations): ")
    
    print(f"To support your goal of {goal}, try the following environment changes: {environment_tips}")

def habit_stacking():
    new_habit = input("Enter the new habit you want to develop: ")
    existing_habit = input("Enter an existing habit you can stack it with: ")
    
    print(f"Try doing {new_habit} right before or after {existing_habit} to make it easier to remember.")

def cues_and_reminders():
    habit = input("Enter the habit you want to develop: ")
    reminder = input("Enter a cue or reminder you can use (e.g., set a 'get ready for bed' alarm): ")
    
    print(f"To remind yourself to {habit}, use the following cue/reminder: {reminder}")
def random_choice():
    tools = [
        intentional_imperfection, micro_habits, intrinsic_motivation,
        positive_reinforcement, environment_change, habit_stacking, cues_and_reminders
    ]
    choice = random.choice(tools)
    choice()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Behavior Change Tools")
    parser.add_argument("--tool", type=str, choices=[
        "intentional_imperfection", "micro_habits", "intrinsic_motivation",
        "positive_reinforcement", "environment_change", "habit_stacking", "cues_and_reminders", "random"
    ], help="Choose a behavior change tool to use")

    args = parser.parse_args()

    if args.tool == "intentional_imperfection":
        intentional_imperfection()
    elif args.tool == "micro_habits":
        micro_habits()
    elif args.tool == "intrinsic_motivation":
        intrinsic_motivation()
    elif args.tool == "positive_reinforcement":
        positive_reinforcement()
    elif args.tool == "environment_change":
        environment_change()
    elif args.tool == "habit_stacking":
        habit_stacking()
    elif args.tool == "cues_and_reminders":
        cues_and_reminders()
    elif args.tool == "random":
        random_choice()
    else:
        print("Please specify a valid tool using the --tool argument.")


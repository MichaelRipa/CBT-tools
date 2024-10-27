#! /usr/bin/python3

from argparse import ArgumentParser, RawTextHelpFormatter

# Variables

help_str = '''
        SMART Goal tool

        This tool prompts you to check whether a current goal you have is a "SMART" goal: specific, measureable, achievable, relevant, and time-bound.

        Background:

        Before we talk about SMART goals, it’s important to distinguish between outcome goals and process goals.
        Outcome goals are focused on the outcome alone, without specifying what actions you need to take to achieve that outcome, like “start a romantic relationship” or “win a 5 kilometer race.”
        Process goals are goals about your own actions, like “attend two new weekly social activities and introduce myself to people” or “run 3 times per week.”

        Evidence suggests it’s best to combine process and outcome goals. In other words, consider what actions you want to do (process), without losing sight of what you want to happen as a result of your actions (outcome). That way, if your planned actions don’t lead to the desired outcome, you can come up with a different process goal. In one study, people who set a combined process and outcome goal improved their performance by >50%, much more than those who set an outcome goal (17%) or a process goal (30%).

        Acedemic Reference:
        Filby, W. C., Maynard, I. W., & Graydon, J. K. (1999). The effect of multiple-goal strategies on performance outcomes in training and competition. Journal of Applied Sport Psychology, 11(2), 230-246.
        '''

welcome_msg = 'Welcome! This program will run through each component of a "SMART" goal, one at a time. Type "y" when ready'

steps = [
    'Specific: The clearer, the better. “Cut down on sugary beverages” is better than “eat healthier.”',
    'Measurable: This doesn’t mean that your goal needs to include a number, although it can; it just means that it should be easy to determine if you met the goal or not. “Spend only half an hour on social media per day” is better than “cut down on social media”; “ask my spouse how she’s feeling every day” is better than “be more caring.”',
    'Achievable: Challenging but still realistic, given what you know about yourself and your situation. In other words, try to push yourself a little without being too hard on yourself. If you\'ve tried to quit smoking four times before, maybe going cold turkey tomorrow isn\'t realistic, but cutting down on a gradual but strict schedule might be.',
    'Relevant: Is the goal relevant to your values? It helps to remind yourself why the goal is important in order to maintain your motivation, especially when encountering challenges or inconvenience. So, make sure your goal is connected to one of your core values.',
    'Time-bound: Include a deadline—keeping in mind the A for achievable, of course. It’s obvious how to set a deadline if your goal is a one-time action; just specify when that action needs to be complete. But what if you want to develop a new habit, like getting more physical activity or spending less time on social media? In that case, you can set yourself a start date and several benchmarks for smaller goals along the way.'
]

prompt = 'Is your goal'


if __name__ == '__main__':
    parser = ArgumentParser(description=help_str,formatter_class=RawTextHelpFormatter)
    args = parser.parse_args()

    print(welcome_msg)
    inp = ''
    while inp != 'y':
        inp = input()

    print('\n')
    for step in steps:
        input(f'{prompt} {step}\n')

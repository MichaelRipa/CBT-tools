#! /usr/bin/python3

from argparse import ArgumentParser, RawTextHelpFormatter

# Variables

help_str = '''
        Mental contrasting with implementation intentions (MCII)

        MCII is a 5-minute tool for increasing the probability that you will reach a goal. This script carries out an interactive session for going through an MCII using the command-line. 

        Also known as "WOOP", which stands for "wish, outcome, obstacle, plan."

        Acedemic Reference:
        Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta‐analysis of effects and processes. Advances in Experimental Social Psychology, 38, 69-119.
        '''

welcome_msg = 'Welcome! Are you ready to do an MCII exercise? Type "y" when ready'

steps = [
    'Visualize steps to goal. Visualize yourself successfully carrying out the actions to achieve your goal.',
    'Identify obstacles. Now imagine the top 2-4 things that are most likely to get in the way of your goal. Think about obstacles that could arise both in the world around you and within you (i.e., your thoughts, feelings, and behaviors). Forgetting is one of the most common obstacles, so make sure to include that one!',
    'Make if-then plans for obstacles. For each obstacle, come up with a one-sentence plan about what you can do if you encounter it, in the form, “If X happens, then I will Y.” That way, instead of getting stuck, feeling hopeless or acting on impulse when something gets in your way, you’ll instantly know what next step to take.',
    'Visualize if-then plans. Finally, mentally rehearse your if-then plans. Visualize the obstacle happening, and then vividly imagine yourself taking the planned action. This should create associations in your brain that will get activated when an obstacle arises.'
]


if __name__ == '__main__':
    parser = ArgumentParser(description=help_str,formatter_class=RawTextHelpFormatter)
    args = parser.parse_args()

    print(welcome_msg)
    inp = ''
    while inp != 'y':
        inp = input()

    print('\n')
    for i, step in enumerate(steps):
        input(f'{i+1}. {step}\n')

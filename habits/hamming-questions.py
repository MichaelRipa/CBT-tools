import time

def get_input(prompt, timer=None):
    if timer:
        print(f"You have {timer} seconds to answer this question.")
    start_time = time.time()
    response = input(prompt + "\n")
    elapsed_time = time.time() - start_time
    if timer and elapsed_time > timer:
        print("Time's up!")
    return response

def main():
    print("Richard Hamming's Self-Reflection Questions\n")

    timer = input("Would you like to set a timer for each question? Enter the number of seconds or 'no': ").strip().lower()
    timer = int(timer) if timer != 'no' else None

    questions = [
        "Prompt 0: Initial thoughts\nDid anything come up already? Is anything staring you in the face right now? Now that you have the idea of a “Hamming question” in mind: is anything obvious as your most important problem?\nYou might also try: Picturing another person, identical to you, and asking what their main bottleneck is.",
        "Prompt 1: Rate-limiting step\nThe speed of a chemical reaction is determined by the speed of the slowest step—the rate-limiting step. What is yours? Or: what's your bottleneck? Is there a problem where solving it would be the equivalent of “wishing for more wishes?”",
        "Prompt 2: What are you not allowed to care about?\nOr: Is there some good outcome that you generally don't think about because it's too big to picture? Or too impossible?\nConversely, what do you have to care about, even though you'd really rather not/it doesn't feel like where your heart and soul actually want to be?",
        "Prompt 3: Genre-savviness\nWhen you're reading a novel, sometimes it seems like the book is dragging/stuck because there is an obvious thing that the character needs to do next in order to advance the plot (e.g. clearly she needs to go talk to the magician—can't she just do it already?). If your life is a novel: what is that obvious next thing?",
        "Prompt 4: What are you already pursuing, badly, in a convoluted/distorted way?\nPica is a medical condition in which people who are iron deficient (for example) eat things like ice cubes, because the signal to eat things with iron is getting distorted into an urge to eat things which share superficial properties with iron. So: what is everything you're doing a pica for?",
        "Prompt 5: Scope Sensitivity/Magnitude of your problems\nWhich problems in your life have effects that are the largest order of magnitude? You may want to think separately about the effects on you and the effects on the world. For example, for effects on you: If you think about the gap between your current life and a better version of your life, which problem could you solve to cross the largest fraction of that gap? Or, for effects on the world: If you think about the size of your positive impact on the world, which problem could you solve to increase that impact by the largest amount?",
        "Prompt 6: Gendlin's Focusing check\nSay aloud: “My life is fine.” (Or: “I feel all fine and good about my life.”)\nIf you're like most people, something will catch in your throat. Write it down.\nThen imagine putting that thing next to you on the park bench, and go again: “Apart from [that thing], my life is fine in all respects.” See what catches now.\nFor most people, something will catch maybe 3-5 times, and then the sentence will ring true. (“Apart from A, B, C, and D, my life really is fine.”)",
        "Prompt 7: Spinning plates\nWhat captures your curiosity the way that the spinning plate captured Feynman's curiosity? What do you find your attention drawn to? What feels interesting to your system 1?",
        "Prompt 8: Final go\nSo, having now gone through all of that: What feels most alive? What is the most important problem, for you, right now?"
    ]

    responses = []

    for question in questions:
        response = get_input(question, timer)
        responses.append(response)
        print("\n")

    print("Thank you for your responses. Here is a summary of your answers:\n")
    for i, response in enumerate(responses):
        print(f"Response to Prompt {i}: {response}\n")

if __name__ == "__main__":
    main()

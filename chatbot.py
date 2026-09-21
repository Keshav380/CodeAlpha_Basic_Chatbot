"""
CodeAlpha Internship - Task 4
Basic Rule-Based Chatbot

A simple console chatbot that replies to the user using predefined rules.
No machine learning is used - the bot understands the user by looking for
keywords in the input and choosing a matching reply.

Concepts used: functions, if-elif, loops, input/output, lists, dictionaries.

Author: <your name>
"""

import random
import datetime


BOT_NAME = "Alpha"

# ---------------------------------------------------------------------------
# Rule table
# Each rule is a tuple: (list of keywords, list of possible replies)
# Several replies are given so the bot does not sound repetitive.
# ---------------------------------------------------------------------------
RULES = [
    (
        ["hello", "hi", "hey", "hii", "heya", "good morning", "good evening"],
        ["Hi there!", "Hello! Nice to see you.", "Hey! How can I help you today?"],
    ),
    (
        ["how are you", "how r u", "how do you do", "whats up", "what's up"],
        ["I'm fine, thanks! How about you?", "Doing great! What about you?"],
    ),
    (
        ["your name", "who are you", "what are you"],
        [f"My name is {BOT_NAME}, a simple rule-based chatbot.",
         f"I'm {BOT_NAME}. I was built for the CodeAlpha internship."],
    ),
    (
        ["help", "what can you do", "options"],
        ["You can greet me, ask my name, ask the time or date, "
         "ask about CodeAlpha, or type 'bye' to exit."],
    ),
    (
        ["codealpha", "internship", "task"],
        ["CodeAlpha is where I was built - this chatbot is Task 4 of the "
         "Python programming internship.",
         "I'm part of a CodeAlpha internship project on rule-based chatbots."],
    ),
    (
        ["thanks", "thank you", "thx"],
        ["You're welcome!", "Happy to help!", "Anytime!"],
    ),
    (
        ["joke", "funny"],
        ["Why do programmers prefer dark mode? Because light attracts bugs!",
         "There are 10 kinds of people: those who know binary and those who don't."],
    ),
    (
        ["weather", "rain", "temperature"],
        ["I can't check the weather yet - I only know the rules I was given."],
    ),
    (
        ["bye", "goodbye", "exit", "quit", "see you"],
        ["Goodbye!", "See you later!", "Bye! Have a nice day."],
    ),
]

# Replies used when no rule matches the user input
FALLBACK_REPLIES = [
    "Sorry, I didn't understand that. Type 'help' to see what I know.",
    "Hmm, that's outside my rules. Try asking something else.",
    "I'm not sure how to reply to that yet.",
]

EXIT_WORDS = ["bye", "goodbye", "exit", "quit", "see you"]


def clean_input(text):
    """Lowercase the message and remove punctuation so it is easy to compare."""
    text = text.lower().strip()
    for mark in "?!.,;:":
        text = text.replace(mark, " ")
    # join the words back with single spaces
    return " ".join(text.split())


def matches(user_text, keywords):
    """
    Return True if any keyword appears in the user's message.

    A keyword made of several words (like "how are you") is searched for
    inside the whole sentence. A single word is compared word by word, so
    "hi" does not accidentally match inside "this".
    """
    words = user_text.split()
    for keyword in keywords:
        if " " in keyword:
            if keyword in user_text:
                return True
        elif keyword in words:
            return True
    return False


def get_response(user_text):
    """
    Decide what the bot should reply.

    The message is compared against every rule in order. The first rule
    whose keywords appear in the message wins.
    """
    user_text = clean_input(user_text)

    # if-elif chain for the special cases that need live data
    if user_text == "":
        return "You didn't type anything. Say something!"
    elif "time" in user_text:
        return "The time is " + datetime.datetime.now().strftime("%I:%M %p") + "."
    elif "date" in user_text or "day today" in user_text:
        return "Today is " + datetime.datetime.now().strftime("%d %B %Y") + "."

    # Normal keyword rules
    for keywords, replies in RULES:
        if matches(user_text, keywords):
            return random.choice(replies)

    # Nothing matched
    return random.choice(FALLBACK_REPLIES)


def is_exit(user_text):
    """Return True if the user wants to end the conversation."""
    return matches(clean_input(user_text), EXIT_WORDS)


def save_log(conversation):
    """Save the whole conversation to a text file."""
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write("--- Chat on " +
                   datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p") + " ---\n")
        for line in conversation:
            file.write(line + "\n")
        file.write("\n")


def show_welcome():
    """Print the opening banner."""
    print("=" * 50)
    print(f"        {BOT_NAME} - Basic Rule-Based Chatbot")
    print("        CodeAlpha Internship | Task 4")
    print("=" * 50)
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")


def chat():
    """Main conversation loop."""
    show_welcome()
    conversation = []

    while True:
        user_text = input("You: ")
        conversation.append("You: " + user_text)

        if is_exit(user_text):
            reply = get_response(user_text)
            print(f"{BOT_NAME}: {reply}")
            conversation.append(f"{BOT_NAME}: {reply}")
            break

        reply = get_response(user_text)
        print(f"{BOT_NAME}: {reply}\n")
        conversation.append(f"{BOT_NAME}: {reply}")

    save_log(conversation)
    print("\nChat saved to chat_log.txt. Thanks for talking to me!")


if __name__ == "__main__":
    chat()

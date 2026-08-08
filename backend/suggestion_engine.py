import re

REPLACEMENTS = {
    "idiot": "person",
    "stupid": "mistaken",
    "dumb": "misinformed",
    "moron": "person",
    "hate you": "disagree with you",
    "fuck you": "I strongly disagree with you.",
    "shut up": "Let's discuss calmly.",
    "go to hell": "I don't agree with your opinion.",
    "kill yourself": "Please take care of yourself."
}


def generate_suggestion(text):

    suggestion = text

    for old, new in REPLACEMENTS.items():
        suggestion = re.sub(
            old,
            new,
            suggestion,
            flags=re.IGNORECASE
        )

    return suggestion
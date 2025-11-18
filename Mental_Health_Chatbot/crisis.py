from typing import List

CRISIS_KEYWORDS: List[str] = [
    "suicide",
    "kill myself",
    "end my life",
    "want to die",
    "hopeless",
    "worthless",
    "no reason to live",
    "give up",
    "can't go on",
    "overwhelmed",
    "desperate",
    "self-harm",
    "cutting",
    "hurt myself",
    "depressed",
    "depression",
    "anxiety",
    "panic attack",
    "mental breakdown",
    "crisis",
    "need help now"
]

SAFETY_MESSAGE = (
    "It seems like you're going through a really tough time right now. "
    "Please remember that you're not alone, and there are people who care about you and want to help. "
    "If you're feeling overwhelmed, consider reaching out to a mental health professional or a trusted person in your life. "
    "In case of an emergency, please contact emergency services or a crisis hotline immediately. "
    "**India:** 9152987821 (icall), 1800-599-0019 (Vandrevala Foundation)\n"
    "**USA:** 988 (National Suicide Prevention Lifeline)\n"
    "**UK:** 116 123 (Samaritans)\n\n"
    "You matter."
)

def contains_crisis_keywords(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)

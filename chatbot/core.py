from typing import List, Dict

class Conversation:
    """Simple in-memory conversation history. Each entry is a dict: {'role': 'user'|'bot', 'text': str}"""
    def __init__(self):
        self._messages = []

    def add_user_message(self, text: str):
        self._messages.append({'role': 'user', 'text': text})

    def add_bot_message(self, text: str):
        self._messages.append({'role': 'bot', 'text': text})

    def get_messages(self) -> List[Dict]:
        return list(self._messages)

    def get_user_messages(self) -> List[str]:
        return [m['text'] for m in self._messages if m['role'] == 'user']

    def clear(self):
        self._messages.clear()


class Chatbot:
    """Very small rule-based chatbot. Replaceable with something fancier later."""
    def __init__(self):
        pass

    def reply_to(self, user_text: str) -> str:
        t = user_text.lower()
        if any(w in t for w in ['help', 'support', 'issue', 'problem']):
            return "I hear you — tell me more about the issue and I’ll try to help."
        if any(w in t for w in ['thank', 'thanks']):
            return "You’re welcome. Anything else I can do?"
        if any(w in t for w in ['hello', 'hi']):
            return "Hi there. How can I help today?"
        if any(w in t for w in ['bye', 'goodbye']):
            return "Goodbye — feel better soon."
        # fallback
        return "Got it. Can you elaborate a bit more?"

from typing import List, Dict
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        # ensure the user ran: python -m nltk.downloader vader_lexicon
        self._analyzer = SentimentIntensityAnalyzer()

    def analyze_statement(self, text: str) -> Dict:
        """Return VADER scores and a label for a single statement."""
        scores = self._analyzer.polarity_scores(text)
        label = self._label_from_compound(scores['compound'])
        return {'text': text, 'scores': scores, 'label': label}

    def analyze_conversation(self, messages: List[Dict]) -> Dict:
        """Aggregate conversation-level sentiment by averaging compound scores of user messages."""
        user_texts = [m['text'] for m in messages if m['role'] == 'user']
        if not user_texts:
            return {'label': 'Neutral', 'average_compound': 0.0, 'count': 0}

        compounds = [self._analyzer.polarity_scores(t)['compound'] for t in user_texts]
        avg = sum(compounds) / len(compounds)
        label = self._label_from_compound(avg)
        return {'label': label, 'average_compound': avg, 'count': len(compounds)}

    def compute_trend(self, user_texts: List[str]) -> Dict:
        """Compute trend: compares first half avg vs second half avg to detect shift."""
        n = len(user_texts)
        if n < 2:
            return {'trend': 'No clear trend', 'details': None}
        mid = n // 2
        first = user_texts[:mid]
        second = user_texts[mid:]
        first_avg = sum(self._analyzer.polarity_scores(t)['compound'] for t in first) / len(first)
        second_avg = sum(self._analyzer.polarity_scores(t)['compound'] for t in second) / len(second)
        diff = second_avg - first_avg
        if diff > 0.05:
            trend = 'Improving'
        elif diff < -0.05:
            trend = 'Worsening'
        else:
            trend = 'Stable'
        return {'trend': trend, 'first_avg': first_avg, 'second_avg': second_avg, 'diff': diff}

    @staticmethod
    def _label_from_compound(compound: float) -> str:
        if compound >= 0.05:
            return 'Positive'
        if compound <= -0.05:
            return 'Negative'
        return 'Neutral'

from chatbot.sentiment import SentimentAnalyzer


sa = SentimentAnalyzer()




def test_statement_positive():
r = sa.analyze_statement('I love this product, it is great!')
assert r['label'] == 'Positive'




def test_statement_negative():
r = sa.analyze_statement('This was awful and disappointing')
assert r['label'] == 'Negative'




def test_conversation_aggregate():
msgs = [
{'
from flask import Flask, render_template, request, jsonify
from chatbot.core import Chatbot, Conversation
from chatbot.sentiment import SentimentAnalyzer

app = Flask(__name__)

# single chatbot instance for demo
sentiment = SentimentAnalyzer()
bot = Chatbot()
conv = Conversation()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/message', methods=['POST'])
def message():
    data = request.json or {}
    user_text = data.get('text', '').strip()
    if not user_text:
        return jsonify({'error': 'No text provided'}), 400

    # append user message
    conv.add_user_message(user_text)

    # statement-level sentiment
    stmt_sent = sentiment.analyze_statement(user_text)

    # bot replies (simple logic)
    reply = bot.reply_to(user_text)
    conv.add_bot_message(reply)

    # conversation-level sentiment (Tier 1)
    convo_sent = sentiment.analyze_conversation(conv.get_messages())

    # optional: compute trend across statements
    trend = sentiment.compute_trend(conv.get_user_messages())

    return jsonify({
        'reply': reply,
        'statement_sentiment': stmt_sent,
        'conversation_sentiment': convo_sent,
        'trend': trend,
        'history': conv.get_messages()
    })


if __name__ == '__main__':
    app.run(debug=True)

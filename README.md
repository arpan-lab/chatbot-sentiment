# Chatbot with Sentiment Analysis

A Python-based chatbot that analyzes the sentiment of user messages. It performs **conversation-level** and **statement-level** sentiment evaluation using **NLTK's VADER** sentiment analyzer.

## Features
- Conversation-level sentiment analysis (Tier 1)
- Statement-level sentiment analysis for each user message (Tier 2)
- Trend analysis across the conversation (Stable / Improving / Worsening)
- Simple, modular Python code (`core.py`, `sentiment.py`)
- Flask web interface with interactive chat

## Technologies
- Python 3.x
- Flask
- NLTK (VADER)
- HTML / JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/chatbot-sentiment.git
cd chatbot-sentiment
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

powershell
Copy code
.\venv\Scripts\Activate   # Windows
# source venv/bin/activate # macOS/Linux
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Download VADER lexicon for NLTK:

bash
Copy code
python -m nltk.downloader vader_lexicon
Usage
Run the Flask app:

bash
Copy code
python app.py
Open a browser at:

cpp
Copy code
http://127.0.0.1:5000
Type messages to chat with the bot and see sentiment analysis results in real time.

Example Output
yaml
Copy code
User: "I love this service!"
Statement sentiment: Positive (0.669)
Conversation sentiment: Positive (avg 0.669)
Trend: Improving

User: "This is frustrating."
Statement sentiment: Negative (-0.659)
Conversation sentiment: Neutral (avg 0.005)
Trend: Worsening
Status
Tier 1: Complete ✅

Tier 2: Implemented ✅

Trend analysis: Implemented ✅

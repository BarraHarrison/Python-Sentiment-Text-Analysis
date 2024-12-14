# Sentiment Text Analysis using Python
import nltk
nltk.download('punkt')
from textblob import TextBlob
from newspaper import Article


with open('example-text.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(f"Sentiment Polarity: {sentiment}")
# Sentiment Text Analysis using Python
import nltk
nltk.data.path.append('/Users/barraharrison/nltk_data')  
nltk.download('punkt')  
from textblob import TextBlob


with open('example-text.txt', 'r') as f:
    text = f.read()


blob = TextBlob(text)


sentiment = blob.sentiment.polarity
print(f"Sentiment Polarity: {sentiment}")

# Tokenize words manually and analyze sentiment for each word
positive_words = []
negative_words = []

words = text.split()  # Fallback: Basic tokenization
for word in words:
    word_sentiment = TextBlob(word).sentiment.polarity
    if word_sentiment > 0:
        positive_words.append(word)
    elif word_sentiment < 0:
        negative_words.append(word)

# Print contributing words
print("\nPositive Words:")
print(", ".join(positive_words) if positive_words else "None")

print("\nNegative Words:")
print(", ".join(negative_words) if negative_words else "None")

# Sentiment Text Analysis using Python
import nltk
nltk.download('punkt')
from textblob import TextBlob
from newspaper import Article


url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
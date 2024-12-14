## Python Sentiment Text Analysis

# Brief Description
This Python program performs sentiment analysis on text data, analyzing the overall sentiment and identifying words contributing to the sentiment.
The program uses the TextBlob library for natural language processing and sentiment analysis.
It processes an input text file (example-text.txt), calculates the overall sentiment polarity, and identifies the positive and negative words in the text.

## How does the code even work?

# Input File:
The program reads the content of a text file named example-text.txt. This file should contain the text you want to analyze.

# Overall Sentiment Analysis:
Using TextBlob, the program calculates the sentiment polarity of the text:
- Polarity ranges from -1.0 (very negative) to 1.0 (very positive).
- A score close to 0 indicates a neutral sentiment.

# Word-Level Analysis:
The program tokenizes the text into individual words and evaluates each word's sentiment polarity.
- Positive words are words with a positive polarity (> 0).
- Negative words are words with a negative polarity (< 0).

# The Program Prints:
- The overall sentiment polarity of the text.
- A list of positive words in the text.
- A list of negative words in the text.

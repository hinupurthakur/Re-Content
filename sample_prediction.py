from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
opinion = TextBlob("EliteDataScience.com is depressed!", analyzer=NaiveBayesAnalyzer())
print(opinion.sentiment)

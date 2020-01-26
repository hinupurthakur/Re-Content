from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)


inp = input("Enter something:")

positive = 0
negative = 0
neutral = 0
polarity = 0


for word in inp:
    analyzer = TextBlob(word)
    polarity += analyzer.sentiment.polarity
    if analyzer.sentiment.polarity > 0:
    	positive += 1
    elif analyzer.sentiment.polarity < 0:
    	negative += 1
    elif analyzer.sentiment.polarity == 0:
    	neutral += 1

positive = percentage(positive,(positive + negative + neutral))
negative = percentage(negative,(positive + negative + neutral))
neutral = percentage(neutral,(positive + negative + neutral))

positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')

if (polarity > 0):
    print("Positive")
elif (polarity < 0):
    print("Negative")
elif (polarity == 0):
    print("Neutral")

labels = ['Positive ['+str(positive)+'%]', 'Negative ['+str(negative)+'%]', 
'Neutral ['+str(neutral)+'%]']
sizes = [positive, negative, neutral]
colors = ['blue','red','yellow']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("Polarity Pie Chart")
plt.axis('equal')
plt.tight_layout()
plt.show()

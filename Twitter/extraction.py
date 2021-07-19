import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = '714460750173962240-Z0rJynuMCJUN1ajxWjS2Rz6DTTcfWNo'
access_token_secret = '1seLcRJOS4V5yvceQoZkSFo4lLbcseq8rQT5tGejaB6pv'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@imnupurthakur', tweet_mode="extended").items():
    print(status.full_text)

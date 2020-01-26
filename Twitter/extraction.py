import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'wIMAr52yVySpGc7uZcdtjRMwT'
consumer_secret = '1kI0l7Wn5yXW5W4s2RIYYzOUhpvvXyfqN1dfdGhqQfjAkgUG2z'
access_token = '714460750173962240-pFSCIiTikGtorLHskgg48PL9Zjkc7yC'
access_token_secret = '9lYsD14k1Sg1rZ7QLiD7CLRQ9fwNP26514d4ocJ3f9NFj'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@imnupurthakur', tweet_mode="extended").items():
    print(status.full_text)

# Import the module
import tweepy

# Assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# Calling the api
api = tweepy.API(auth)

# The ID of the tweet to be retweeted
ID =

# Retweeting the tweet
api.retweet(ID)

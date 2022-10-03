import tweepy 
# personal details 
my_consumer_key ="customer_key"
my_consumer_secret ="secret_no"
my_access_token ="token_no"
my_access_token_secret ="secret_token"
# authentication of consumer key and secret 
my_auth = tweepy.OAuthHandler(my_consumer_key, my_consumer_secret) 
# Authentication of access token and secret 
my_auth.set_access_token(my_access_token, my_access_token_secret) 
my_api = tweepy.API(my_auth)
my_api.update_status(status="Your desired tweet")

# import the module
import tweepy
  
# assign the values accordingly
consumer_key = ""            # enter the respective API's inside the Quotation marks
consumer_secret = ""         # enter the respective API's inside the Quotation marks
access_token = ""            # enter the respective API's inside the Quotation marks
access_token_secret = ""     # enter the respective API's inside the Quotation marks
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # don't fill the API here
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)   # don't fill the API here
  
# calling the api 
api = tweepy.API(auth)

print("What would you like to say with your image?") 
# the text to be tweeted
status = input("What would you like to say with your image?")   # enter your desired text to be tweeted
  
# the path of the media to be uploaded
filename = input("What is thge direct path for your image?")
  
# posting the tweet
api.update_with_media(filename, status)
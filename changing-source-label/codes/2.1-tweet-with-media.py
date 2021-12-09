import tweepy
auth = tweepy.OAuthHandler("CONSUMER KEY HERE", "CONSUMER KEY SECRET HERE")
auth.set_access_token("ACCESS TOKEN HERE", "ACCESS TOKEN SECRET HERE")
api = tweepy.API(auth)
tweet = input("")
image="C:/Users/image.jpg"  #Enter image location
api.update_with_media(image, tweet)
print ("Your tweet has been tweeted !")

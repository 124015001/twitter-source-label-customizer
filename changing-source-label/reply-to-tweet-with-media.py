# the text to be tweeted
status = "This is a tweet is a reply."
   
# the ID of the tweet to be replied to
in_reply_to_status_id = ""
  
# the path of the media to be uploaded
filename = "gfg.png"
  
# posting the tweet
api.update_with_media(filename, status, in_reply_to_status_id = in_reply_to_status_id)

import tweepy
import time
import random
 
# Consumer keys and access tokens, used for OAuth
consumer_key = ""
consumer_secret = "" 
access_token = ""
access_token_secret = "" 
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
 
# Sample method, used to update a status
#api.update_status('Hello Python Central!')


f = open("actual.txt", "r")
#line = f.readline()

def follow_action():
    x = random.randrange(100,2000)
    print(x)
    cnt = (f.readline())
    print(cnt)
    try:
        api.create_friendship(cnt)
        time.sleep(x)
    except:
        follow_action()
        time.sleep(x)
    

    
    

while 1:
    follow_action()
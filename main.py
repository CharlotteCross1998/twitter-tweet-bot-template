import tweepy, oauth

words = []

c_key = ""
c_secret = ""
a_key = ""
a_secret = ""

auth = tweepy.OAuthHandler(c_key,c_secret)
auth.set_access_token(a_key,a_secret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

import random, time

with open ('words.txt', 'r') as file:
  words = file.read().split(' ') #words are split by space in this example
  
while True:
  api.update_status(random.choice(words))
  time.sleep(1800)

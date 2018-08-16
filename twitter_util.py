import tweepy
import datetime


#Auth Keys
consumer_key = "EgmeUYeuC2SMjw2OnFty5LRS9"
consumer_secret = "fImnylmtR5X8eBYZclmrj0tof2USR8geVfEa8t2gEIbsMuiHRz"

access_token = "1022239524607254528-bK0SXoiuAKKZZaPL58i1wt370SI14w"
access_token_secret = "QGVC06EK9maRYXmTb8HU2x5zLYxDK8V0SYN8numNk0wUD"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline('@bagholderquotes',count=100)


for tweet in public_tweets:
    print(tweet.created_at.isoformat() + ", " + tweet.text)


# function to work one guys twitter



# function to do one ticker twitter

# function to loop through tweets to get more than one request
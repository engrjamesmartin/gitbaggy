import tweepy
import datetime
from datetime import timedelta


#Auth Keys
consumer_key = "EgmeUYeuC2SMjw2OnFty5LRS9"
consumer_secret = "fImnylmtR5X8eBYZclmrj0tof2USR8geVfEa8t2gEIbsMuiHRz"

access_token = "1022239524607254528-bK0SXoiuAKKZZaPL58i1wt370SI14w"
access_token_secret = "QGVC06EK9maRYXmTb8HU2x5zLYxDK8V0SYN8numNk0wUD"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# function to work one guys twitter
def get_user_tweets(username,window,baggy):
    public_tweets = api.user_timeline(id=username,count=100)
    oldest = public_tweets[-1].id

    resultset = []

    for tweet in public_tweets:
        resultset.append([tweet.id, tweet.text, tweet.created_at, "baggy"])

    while((datetime.datetime.now() - timedelta(days=window)) < public_tweets[-1].created_at):
        print("getting tweets before " + str(oldest))
        public_tweets = api.user_timeline(id=username,count=100,max_id=oldest)
        oldest = public_tweets[-1].id

        for tweet in public_tweets:
            resultset.append([tweet.id,tweet.text,tweet.created_at,baggy])


    print("Total Tweets: " + str(len(resultset)))

    return resultset
    # for tweet in public_tweets:
    #     print(tweet.created_at.isoformat() + ", " + tweet.text)


# function to do one ticker twitter


get_user_tweets('@bagholderquotes',20,'baggy')
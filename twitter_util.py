import tweepy
import datetime
import tokens
from datetime import timedelta


#Auth Keys
consumer_key = tokens.consumer_key
consumer_secret = tokens.consumer_secret

access_token = tokens.access_token
access_token_secret = tokens.access_token_secret

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


# function to do one ticker twitter
def get_ticker_tweets(ticker,window,baggy):
    public_tweets = api.search(q=ticker,count=100)
    oldest = public_tweets[-1].id

    resultset = []

    for tweet in public_tweets:
        resultset.append([tweet.id, tweet.text, tweet.created_at, "baggy"])

    while((datetime.datetime.now() - timedelta(days=window)) < public_tweets[-1].created_at):
        print("getting tweets before " + str(oldest))
        public_tweets = api.search(q=ticker,count=100,max_id=oldest)
        oldest = public_tweets[-1].id

        for tweet in public_tweets:
            resultset.append([tweet.id,tweet.text,tweet.created_at,baggy])


    print("Total Tweets: " + str(len(resultset)))

    return resultset

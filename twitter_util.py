import tweepy
import datetime
import tokens
from datetime import timedelta
from tensor_util import use_model


#Auth Keys
#note, you need the tokens.py file, in that file have the keys equal to your twitter keys. Example:
# consumer_key = "my twitter consumer key"
consumer_key = tokens.consumer_key
consumer_secret = tokens.consumer_secret

access_token = tokens.access_token
access_token_secret = tokens.access_token_secret

#create the auth token
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# function to work one guys twitter
def get_user_tweets(username,baggy,days=1,hours=0):
    public_tweets = api.user_timeline(id=username,count=100)
    oldest = public_tweets[-1].id

    resultset = []

    for tweet in public_tweets:
        resultset.append([tweet.id, tweet.text, tweet.created_at, baggy])

    while((datetime.datetime.now() - timedelta(days=days,hours=hours)) < public_tweets[-1].created_at):
        print("getting tweets before " + str(oldest))
        public_tweets = api.user_timeline(id=username,count=100,max_id=oldest)
        oldest = public_tweets[-1].id

        for tweet in public_tweets:
            resultset.append([tweet.id,tweet.text,tweet.created_at,baggy])


    print("Total Tweets: " + str(len(resultset)))

    return resultset


# function to do one ticker twitter
def get_ticker_tweets(ticker,baggy,days=0,hours=0):
    public_tweets = api.search(q=ticker,count=100)
    oldest = public_tweets[-1].id

    #amazon has a lot of tweets, making a special case
    if(ticker=="$AMZN"):
        days=0
        hours=12

    resultset = []

    for tweet in public_tweets:
        resultset.append([tweet.id, tweet.text, tweet.created_at, baggy])

    while((datetime.datetime.now() - timedelta(days=days,hours=hours)) < public_tweets[-1].created_at):
        print("getting tweets before " + str(oldest))
        public_tweets = api.search(q=ticker,count=100,max_id=oldest)
        oldest = public_tweets[-1].id

        for tweet in public_tweets:
            resultset.append([tweet.id,tweet.text,tweet.created_at,baggy])


    print("Total Tweets: " + str(len(resultset)))

    return resultset


#this function will open a stream with twitter on a username
def get_stream(username, estimator):
    class MyStreamListener(tweepy.StreamListener):
        def on_status(self, status):
            if (str(use_model(estimator=estimator,tweet=status.text)) =="0"):
                print("Not Baggy : " + status.text)
            else:
                print("Baggy     : " + status.text)
            #print(status.text)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

    myStream.filter(track=[username])
import twitter_util as twitter

#need to have my library for twitter already created
#neet to have my library for tensorflow stuff created



#pass to functions in my twitter lib
bagholder_user = '@bagholderquotes'
non_bagholder_ticker = ['$AMZN']

twitter.get_user_tweets(bagholder_user,20,'baggy')
for ticker in non_bagholder_ticker:
    twitter.get_ticker_tweets(ticker,1,'not baggy')

#pass to functions in my tensorflow lib

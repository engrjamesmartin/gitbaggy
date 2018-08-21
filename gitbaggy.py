import twitter_util as twitter
import tensor_util as tensor

#need to have my library for twitter already created
#neet to have my library for tensorflow stuff created



#pass to functions in my twitter lib
bagholder_user = '@bagholderquotes'
non_bagholder_ticker = ['$AMZN']

training_data = twitter.get_user_tweets(bagholder_user,'baggy',days=20)


for ticker in non_bagholder_ticker:
    training_data += twitter.get_ticker_tweets(ticker,'not baggy',hours=6)

tensor.train_test_model(training_data)

#pass to functions in my tensorflow lib

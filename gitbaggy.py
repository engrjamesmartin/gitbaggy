import twitter_util as twitter
import tensor_util as tensor
import numpy as np

#need to have my library for twitter already created
#neet to have my library for tensorflow stuff created



#pass to functions in my twitter lib
bagholder_user = '@bagholderquotes'
non_bagholder_ticker = ['$AMZN','$NVDA','$ISRG','$COP']


print("Welcome to gitbaggy")
print("-------------------")
print("1) The monthly bagholder report")
print("2) Train my bagholder")
print("3) Monitor bagholders in the wild")
print("4) Exit")
menu=input("Which analytics would you like to run?: ")

menu=str(menu)

#get non bagholders 0 = not baggy
if(menu=='1'):
    print("Work in progress")
    # get bagholders 1 = baggy
    raw_data = twitter.get_user_tweets(bagholder_user, 'baggy', days=30)

    tickers = []
    for item in raw_data:
        for word in item[1].split():
            if ((word.startswith("$"))&(len(word)>1)):
                if(word[1].isnumeric()!=True):
                    tickers.append(word.strip("!,.?"))

    ticker_count=np.unique(tickers, return_counts=True)

    print(np.array(ticker_count).transpose())

if(menu=='2'):
    # get bagholders 1 = baggy
    training_data = twitter.get_user_tweets(bagholder_user, 1, days=10)

    # get the non bagholders 0 = not baggy
    for ticker in non_bagholder_ticker:
        training_data += twitter.get_ticker_tweets(ticker,0,hours=12)

    print("Total Tweets: " + str(len(training_data)))

    estimator = tensor.train_test_model(training_data)
    print("Work in progress")
    twitter.get_stream("$TSLA", estimator)

if(menu=='3'):
    print("Work in progress")
    twitter.get_stream("$TSLA")
else:
    print("Thank you for visiting the baggies")
#pass to functions in my tensorflow lib

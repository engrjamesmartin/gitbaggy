import tensorflow as tf
import pandas as pd
import numpy as np



def split_list(mylist):
    list_a = []
    list_b = []
    counter = 0

    for item in mylist:
        if (counter % 2 == 0):
            list_a.append(item)
        else:
            list_b.append(item)

    return list_a, list_b

def make_dataframe(mytweets):
    tweets = []
    is_baggy = []
    index = []

    for items in mytweets:
        index.append(items[0])
        tweets.append(items[1])
        is_baggy.append(items[3])

    d = {'tweet': tweets, 'is_baggy': is_baggy}

    df = pd.DataFrame(data=d, index=index)

    return df


def train_test_model(training_data):
    train_df, test_df = split_list(training_data)

    train_df = make_dataframe(train_df)
    test_df = make_dataframe(test_df)

    # do training input
    train_input_fn = tf.estimator.inputs.pandas_input_fn(train_df, train_df["is_baggy"], num_epochs=None, shuffle=True)

    # do testing input
    predict_train_input_fn = tf.estimator.inputs.pandas_input_fn(train_df, train_df["is_baggy"], shuffle=False)

    # prediction on test
    predict_test_input_fn = tf.estimator.inputs.pandas_input_fn(test_df, test_df["is_baggy"], shuffle=False)






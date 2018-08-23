import tensorflow as tf
import tensorflow_hub as hub
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
        counter+=1

    return list_a, list_b

def make_dataframe(mytweets):

    tweets = []
    is_baggy = []
    index = []


    for items in mytweets:
        index.append(items[0])
        tweets.append(items[1])
        is_baggy.append(int(items[3]))

    d = dict(tweet=tweets, is_baggy=is_baggy)

    df = pd.DataFrame(data=d, index=index)

    print(df.dtypes)

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

    embedded_text_feature_column = hub.text_embedding_column(
        key="tweet",
        module_spec="https://tfhub.dev/google/nnlm-en-dim128/1")

    estimator = tf.estimator.DNNClassifier(
        hidden_units=[500,100],
        feature_columns=[embedded_text_feature_column],
        n_classes=2,
        optimizer=tf.train.AdagradOptimizer(learning_rate=0.03)
    )

    print("got past estimator")
    input("stop here")

    estimator.train(input_fn=train_input_fn, steps=100)

    print("got past train")

    train_eval_result = estimator.evaluate(input_fn=predict_train_input_fn)
    test_eval_result = estimator.evaluate(input_fn=predict_test_input_fn)

    print("Training set accuracy: {accuracy}".format(**train_eval_result))
    print("Test set accuracy: {accuracy}".format(**test_eval_result))


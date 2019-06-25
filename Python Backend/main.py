import numpy as np
from sklearn.preprocessing import MinMaxScaler

from lstm import compile_lstm
from preprocess_data import preprocess_data

# To download datasets, run:
# python network\download_datasets.py

import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

TIME_STEPS = 10  # minutes
EPOCHS = 5  # this will increase dramatically
BATCH_SIZE = 1024

stocks = preprocess_data()

amzn = stocks[0]
appl = stocks[1]


def train(stock):
    training_set = stock.iloc[:, :].values
    training_set = MinMaxScaler().fit_transform(training_set)

    X_train, y_train = [], []
    for i in range(TIME_STEPS, len(stock)):
        X_train.append(training_set[i - TIME_STEPS:i])
        y_train.append(training_set[i][0])

    X_train, y_train = np.array(X_train), np.array(y_train)

    n_rows, n_cols, n_predictors = X_train.shape[0], X_train.shape[1], len(X_train[0][0])
    X_train = np.reshape(X_train, (n_rows, n_cols, n_predictors))  # here we add the other variables :0

    lstm = compile_lstm(input_shape=(n_cols, n_predictors))
    lstm.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)


print("TRAINING AMAZON")
train(amzn)
print("TRAINING APPLE")
train(appl)

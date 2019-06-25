import numpy as np
from sklearn.preprocessing import MinMaxScaler

from lstm import compile_lstm
from preprocess_data import preprocess_data

# To download datasets, run:
# python network\download_datasets.py

TIME_STEPS = 5 # minutes
EPOCHS = 5 # this will increase dramatically
BATCH_SIZE = 1024

stocks = preprocess_data()
amzn = stocks[0]

#print(amzn.iloc[0])
#print(amzn.iloc[1])
#print(amzn.iloc[2])

training_set = amzn.iloc[:, 1:2].values

scaler = MinMaxScaler()
#training_set = scaler.fit_transform(training_set)

X_train = []
y_train = []
for i in range(TIME_STEPS, len(amzn)):
    X_train.append(training_set[i - TIME_STEPS:i, 0])
    y_train.append(training_set[i])

X_train, y_train = np.array(X_train), np.array(y_train)

n_rows, n_cols = X_train.shape[0], X_train.shape[1]
X_train = np.reshape(X_train, (n_rows, n_cols, 1))  # here we add the other variables :0
print(X_train)
print("y_train")
print(y_train)

#lstm = compile_lstm(input_shape=(n_cols, 1))
#lstm.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE)

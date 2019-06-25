from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout


def compile_lstm(input_shape):
    lstm = Sequential()

    lstm.add(LSTM(units=500, return_sequences=True, input_shape=input_shape))
    lstm.add(Dropout(rate=0.2))
    lstm.add(LSTM(units=500, return_sequences=True))
    lstm.add(Dropout(rate=0.2))
    lstm.add(LSTM(units=500, return_sequences=True))
    lstm.add(Dropout(rate=0.2))
    lstm.add(LSTM(units=500))
    lstm.add(Dropout(rate=0.2))
    lstm.add(Dense(units=1))

    lstm.compile(optimizer="adam", loss="mean_squared_error")
    return lstm

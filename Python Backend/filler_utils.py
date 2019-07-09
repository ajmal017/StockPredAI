import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from timeout_utils import timeout


# taken from https://github.com/borisbanushev/stockpredictionai#technicalind
def add_technical_indicators(df):
    # Create 7 and 21 days Moving Average
    df['ma7'] = df['price'].rolling(window=7).mean()
    df['ma21'] = df['price'].rolling(window=21).mean()

    # Create macd
    df['26ema'] = pd.Series.ewm(df['price'], span=26).mean()
    df['12ema'] = pd.Series.ewm(df['price'], span=12).mean()
    df['macd'] = (df['12ema'] - df['26ema'])

    # Create Bollinger Bands
    df['20sd'] = df['price'].rolling(2).std()
    df['upper_band'] = df['ma21'] + (df['20sd'] * 2)
    df['lower_band'] = df['ma21'] - (df['20sd'] * 2)

    # Create Exponential moving average
    df['ema'] = df['price'].ewm(com=0.5).mean()

    # Create Momentum
    df['momentum'] = df['price'] - 1

    return df


def add_fourier_transforms(df):
    close_fft = np.fft.fft(np.asarray(df["price"].tolist()))
    fft_df = pd.DataFrame({'fft': close_fft})
    fft_df['absolute'] = fft_df['fft'].apply(lambda x: np.abs(x))
    fft_df['angle'] = fft_df['fft'].apply(lambda x: np.angle(x))

    plt.figure(figsize=(14, 7), dpi=100)
    fft_list = np.asarray(fft_df['fft'].tolist())
    for num_ in [3, 6, 9]:
        fft_list_m10 = np.copy(fft_list)
        fft_list_m10[num_:-num_] = 0
        np.fft.ifft(fft_list_m10)
        df['fourier' + str(num_)] = np.fft.ifft(fft_list_m10).real
        # print(fft_list_m10)
        '''
        plt.plot(np.fft.ifft(fft_list_m10), label='Fourier transform with {} components'.format(num_))
    plt.plot(df["price"], label='Real')
    plt.xlabel('Minutes')
    plt.ylabel('USD')
    plt.legend()
    plt.show()
    '''


def add_fourier_transforms_with_timeout(df, seconds):
    print("Adding fourier transforms to dataset of size: " + str(len(df)))
    func = timeout(seconds)(add_fourier_transforms)

    try:
        func(df)
        print("Added fourier transforms successfully.")
    except:
        print("Fourier transforms taking more than " + str(seconds) + " seconds. Removing last row...")
        df.drop(df.tail(1).index, inplace=True)
        add_fourier_transforms_with_timeout(df, seconds)


def add_arima(df):
    X = df['price'].values
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=(5, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)

    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)
    '''
    plt.figure(figsize=(12, 6), dpi=100)
    plt.plot(test, label='Real')
    plt.plot(predictions, color='red', label='Predicted')
    plt.xlabel('Days')
    plt.ylabel('USD')
    plt.title('Figure 5: ARIMA model on GS stock')
    plt.legend()
    plt.show()
    '''

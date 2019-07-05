from sklearn.preprocessing import MinMaxScaler

from filler_utils import *
from lstm import compile_lstm
from main_utils import *
from network.fetch_utils_av import *

from network.download_utils import *
from constants import *


def download_starting_data(stock_symbols):
    print("Downloading datasets...")
    for symbol in stock_symbols:
        download_file(BASE_URL, MAP_ENDPOINTS[symbol] + ".zip", STOCKS_LOCATION)
        print(" - " + symbol + " download complete.")

    print("Unzipping datasets...")
    for symbol in stock_symbols:
        unzip_file_and_delete(STOCKS_LOCATION + MAP_ENDPOINTS[symbol] + ".zip")
    print("Unzipping complete.")


def preprocess_data(stock_symbols):
    print("Appending datasets...")
    stocks = []
    for symbol in stock_symbols:
        stocks.append(join_datasets(STOCKS_LOCATION + MAP_ENDPOINTS[symbol] + "/*.csv", with_rows=[0, 1, 5]))
    '''
    print("Formating dates...")
    for stock in stocks:
        format_dates(stock)

    print("Intersecting datasets...")
    crop_dataset_to_frontiers(stocks)
    '''
    for i in range(len(stocks)):
        stocks[i] = stocks[i][[1, 5]]
        stocks[i].rename(columns={1: 'price', 5: 'volume'}, inplace=True)
        stocks[i] = add_technical_indicators(stocks[i])

        print("adding fourier transforms...")
        add_fourier_transforms(stocks[i])
        print("added fourier transforms successfully.")
        stocks[i] = stocks[i].iloc[20:].reset_index(drop=True)
    return stocks
    # Seems that arima is too slow for this dataset
    # add_arima(stocks[i])


def train_data(stocks, time_steps, epochs, batch_size):
    for stock in stocks:
        training_set = stock.iloc[:, :].values
        training_set = MinMaxScaler().fit_transform(training_set)

        x_train, y_train = [], []
        for i in range(time_steps, len(stock)):
            x_train.append(training_set[i - time_steps:i])
            y_train.append(training_set[i][0])

        x_train, y_train = np.array(x_train), np.array(y_train)

        n_rows, n_cols, n_predictors = x_train.shape[0], x_train.shape[1], len(x_train[0][0])
        x_train = np.reshape(x_train, (n_rows, n_cols, n_predictors))  # here we add the other variables :0

        lstm = compile_lstm(input_shape=(n_cols, n_predictors))
        lstm.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)


def fetch_new_data(stock_symbols, time_steps):
    print("Fetching API datasets...")
    stocks = []
    for symbol in stock_symbols:
        print(" - Retrieving " + symbol + " data...")
        i = stock_symbols.index(symbol)

        data = fetch_stock_data(symbol).tail(time_steps + 20)
        data.columns = range(1, 6)

        stocks.append(data[[1, 5]])
        stocks[i].rename(columns={1: 'price', 5: 'volume'}, inplace=True)
        stocks[i] = add_technical_indicators(stocks[i])

        add_fourier_transforms(stocks[i])
        stocks[i] = stocks[i].iloc[20:].reset_index(drop=True)
    return stocks

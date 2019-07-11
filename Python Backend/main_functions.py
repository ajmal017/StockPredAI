from sklearn.preprocessing import MinMaxScaler

from filler_utils import *
from lstm import compile_lstm
from main_utils import *
from network.fetch_utils_av import *
from keras.models import load_model
from sklearn.externals import joblib

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


def preprocess_data(stock_symbols, fast_fourier_timeout_seconds):
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
        add_fourier_transforms_with_timeout(stocks[i], fast_fourier_timeout_seconds)
        stocks[i] = stocks[i].iloc[20:].reset_index(drop=True)
    return stocks
    # Seems that arima is too slow for this dataset
    # add_arima(stocks[i])


def train_data(stock_symbols, stocks, time_steps, epochs, batch_size):

    # we fetch data to MinMax scale the network accordingly
    in_stocks = fetch_new_data(stock_symbols, time_steps)[0]
    stock_index = -1
    for stock in stocks:
        stock_index += 1
        symbol = stock_symbols[stock_index]

        stock = stock.append(in_stocks[stock_index], ignore_index=True)
        stock = stock.append(stock.max().map(lambda x: x*1.5), ignore_index=True)
        stock = stock.append(stock.min().map(lambda x: x * 0.5), ignore_index=True)

        training_set = stock.iloc[:, :].values
        stock.drop(stock.tail((time_steps + 2)).index, inplace=True)

        scaler = MinMaxScaler().fit(training_set)
        if not os.path.exists(SCALERS_LOCATION):
            os.makedirs(SCALERS_LOCATION)
        joblib.dump(scaler, SCALERS_LOCATION + symbol + ".save")

        # finally we save the scaler and delete the mock data (10 fetched and 2 estimated)
        training_set = training_set[:len(training_set)-(time_steps + 2)]
        training_set = scaler.transform(training_set)

        helper_file = open(SCALERS_LOCATION + symbol + "helper.txt", "w")
        l = str(stock["price"][0]) + " " + str(training_set[0][0])
        helper_file.writelines(l)
        helper_file.close()

        x_train, y_train = [], []
        for i in range(time_steps, len(stock)):
            x_train.append(training_set[i - time_steps:i])
            y_train.append(training_set[i][0])

        x_train, y_train = np.array(x_train), np.array(y_train)

        #print(x_train[0])

        n_rows, n_time_steps, n_features = x_train.shape[0], x_train.shape[1], len(x_train[0][0])
        x_train = np.reshape(x_train, (n_rows, n_time_steps, n_features))

        lstm = compile_lstm(input_shape=(n_time_steps, n_features))
        lstm.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

        if not os.path.exists(MODELS_LOCATION):
            os.makedirs(MODELS_LOCATION)
        lstm.save(MODELS_LOCATION + str(symbol) + ".h5")


def load_trained_lstms(stock_symbols):
    lstms = []
    for symbol in stock_symbols:
        lstms.append(load_model(MODELS_LOCATION + symbol + ".h5"))
    return lstms


def fetch_new_data(stock_symbols, time_steps):
    print("Fetching API datasets...")
    stocks = []
    push_stocks = []
    for symbol in stock_symbols:
        print(" - Retrieving " + symbol + " data...")
        i = stock_symbols.index(symbol)

        data = fetch_stock_data(symbol).tail(time_steps + 20)
        data.columns = range(1, 6)

        stocks.append(data[[1, 5]])
        stocks[i].rename(columns={1: 'price', 5: 'volume'}, inplace=True)

        push_stocks.append(data[[1, 2, 3, 4, 5]])
        push_stocks[i].rename(columns={1: 'open', 2: 'close', 3: 'high', 4: 'low', 5: 'volume'}, inplace=True)

        stocks[i] = add_technical_indicators(stocks[i])

        add_fourier_transforms(stocks[i])
        stocks[i] = stocks[i].iloc[20:].reset_index(drop=True)
    return stocks, push_stocks


def evaluate(stock_symbols, in_stocks, batch_size):
    lstms = load_trained_lstms(stock_symbols)

    estimates = []

    stock_index = -1
    for in_stock in in_stocks:
        stock_index += 1
        symbol = stock_symbols[stock_index]

        scaler = joblib.load(SCALERS_LOCATION + symbol + ".save")

        test_set = in_stock.iloc[:, :].values
        test_set = scaler.transform(test_set)

        n_rows, n_cols = test_set.shape[0], test_set.shape[1]
        test_set = np.reshape(test_set, (1, n_rows, n_cols))

        estimates.append(lstms[stock_index].predict(test_set, batch_size))

    return estimates

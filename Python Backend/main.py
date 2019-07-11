from main_functions import *
from network.push_firestore import push_stocks_data

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

STOCK_SYMBOLS = ["AMZN", "INTC"]
TIME_STEPS = 10  # minutes to consider
EPOCHS = 10
BATCH_SIZE = 1024
FAST_FOURIER_TIMEOUT_SECONDS = 20

download_starting_data(STOCK_SYMBOLS)

stocks = preprocess_data(STOCK_SYMBOLS, FAST_FOURIER_TIMEOUT_SECONDS)

train_data(STOCK_SYMBOLS, stocks, TIME_STEPS, EPOCHS, BATCH_SIZE)

in_stocks, push_stocks = fetch_new_data(STOCK_SYMBOLS, TIME_STEPS)

estimates = evaluate(STOCK_SYMBOLS, in_stocks, BATCH_SIZE)

push_stocks_data(STOCK_SYMBOLS, push_stocks, estimates)

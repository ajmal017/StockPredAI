from main_functions import *

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

STOCK_SYMBOLS = ["AMZN", "INTC"]
TIME_STEPS = 10  # minutes to consider
EPOCHS = 5
BATCH_SIZE = 1024

# download_starting_data(STOCK_SYMBOLS)

# stocks = preprocess_data(STOCK_SYMBOLS)

# train_data(stocks, TIME_STEPS, EPOCHS, BATCH_SIZE)

in_stocks = fetch_new_data(STOCK_SYMBOLS, TIME_STEPS)
print(in_stocks)

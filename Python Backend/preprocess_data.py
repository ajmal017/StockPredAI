# -*- coding: utf-8 -*-
from filler_utils import *
from main_utils import *
from network.constants import *
from network.fetch_utils_av import *


def preprocess_data():
    print("Appending datasets...")
    # open, high, low, close, volume, numberOfTrades, weightedAvgPrice from 9:30 to 15:59
    stocks = [
        join_datasets(STOCKS_LOCATION + AMZN_ENDPOINT + "/*.csv", with_rows=[0, 1, 5]),
        join_datasets(STOCKS_LOCATION + APPL_ENDPOINT + "/*.csv", with_rows=[0, 1, 5])
        # join_datasets(STOCKS_LOCATION + INTC_ENDPOINT + "/*.csv", with_rows=[0, 1, 5]),
        # join_datasets(STOCKS_LOCATION + JPM_ENDPOINT + "/*.csv", with_rows=[0, 1, 5]),
        # join_datasets(STOCKS_LOCATION + BAC_ENDPOINT + "/*.csv", with_rows=[0, 1, 5])
    ]

    print("Formating dates...")
    for stock in stocks:
        format_dates(stock)

    print("Intersecting datasets...")
    crop_dataset_to_frontiers(stocks)

    for i in range(0, len(stocks)):
        print(str(len(stocks[i].index)) + " - Every " +
              str(get_time_interval(stocks[i])) + " minutes")

    # we could do something here with the missing data, etc
    # fill_with_avgs(stocks)

    for i in range(len(stocks)):
        prev = stocks[i][[1, 5]]
        stocks[i] = prev  # eliminate dates
        # stocks[i].columns = range(stocks[i].shape[1])
        stocks[i].rename(columns={1: 'Price', 5: 'Volume'}, inplace=True)
        stocks[i] = add_technical_indicators(stocks[i])

        # add_fourier_transforms(stocks[i])
        stocks[i] = stocks[i].iloc[20:].reset_index(drop=True)
        # Seems that arima is too slow for this dataset
        # add_arima(stocks[i])

    return stocks


def fetch_datasets():
    print("Fetching API datasets...")
    in_symbols = ["AMZN", "APPL", "INTC", "JPM", "BAC"]
    in_stocks = []
    for i in range(0, len(in_symbols)):
        symbol = in_symbols[i]
        print("Retrieving " + symbol + " data...")
        in_stocks.append(format_av_data(fetch_stock_data(symbol)))
        print(symbol + " fetch data size: " + str(len(in_stocks[i].index)) + " - Every " +
              str(get_time_interval(in_stocks[i])) + " minutes")

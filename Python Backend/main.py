# -*- coding: utf-8 -*-
from network.constants import *
from main_utils import *
from network.fetch_utils_av import *
from filler_utils import *

# To download datasets, run:
# python network\download_datasets.py

print("Appending datasets...")
# open, high, low, close, volume, numberOfTrades, weightedAvgPrice from 9:30 to 15:59
stocks = [
    join_datasets(STOCKS_LOCATION + AMZN_ENDPOINT + "/*.csv"),
    join_datasets(STOCKS_LOCATION + APPL_ENDPOINT + "/*.csv"),
    join_datasets(STOCKS_LOCATION + INTC_ENDPOINT + "/*.csv"),
    join_datasets(STOCKS_LOCATION + JPM_ENDPOINT + "/*.csv"),
    join_datasets(STOCKS_LOCATION + BAC_ENDPOINT + "/*.csv")]

print("Formating dates...")
for stock in stocks:
    format_dates(stock)

print("Intersecting datasets...")
crop_dataset_to_frontiers(stocks)

# this crops datasets to work as the ones from the API
for i in range(0, len(stocks)):
    stocks[i] = stocks[i].iloc[:, 0: 6]
    print(str(len(stocks[i].index)) + " - Every " +
          str(get_time_interval(stocks[i])) + " minutes")

print("Fetching API datasets...")
in_symbols = ["AMZN", "APPL", "INTC", "JPM", "BAC"]
in_stocks = []
for i in range(0, len(in_symbols)):
    symbol = in_symbols[i]
    print("Retrieving " + symbol + " data...")
    in_stocks.append(format_av_data(fetch_stock_data(symbol)))
    print(symbol + " fetch data size: " + str(len(in_stocks[i].index)) + " - Every " +
          str(get_time_interval(in_stocks[i])) + " minutes")

# fill_with_avgs(stocks)

# -*- coding: utf-8 -*-
from network.constants import *
from main_utils import *
from network.fetch_utils_av import *
from filler_utils import *

# To download datasets, run:
# python network\download_datasets.py

print("Appending datasets...")
# open, high, low, close, volume, numberOfTrades, weightedAvgPrice from 9:30 to 15:59
amzn = join_datasets(STOCKS_LOCATION + AMZN_ENDPOINT + "/*.csv")
appl = join_datasets(STOCKS_LOCATION + APPL_ENDPOINT + "/*.csv")
intc = join_datasets(STOCKS_LOCATION + INTC_ENDPOINT + "/*.csv")

stocks = [amzn, appl, intc]

del amzn, appl, intc

print("Formating dates...")
for stock in stocks:
    format_dates(stock)

print("Intersecting datasets...")
initial_date = find_common_biggest_initial_date(stocks)
final_date = find_common_smallest_final_date(stocks)

for stock in stocks:
    stock = crop_dataset_from_dates(stock, initial_date, final_date)
for i in range(0, len(stocks)):
    stocks[i] = stocks[i].iloc[:, 0: 6]

for stock in stocks:
    print(str(len(stock.index)) + " - Every " +
          str(get_time_interval(stock)) + " seconds")

print("Common start date: " + str(initial_date))
print("Common final date: " + str(final_date))

in_appl = fetch_stock_data("APPL")  # open, high, low, close, volume
in_appl = format_av_data(in_appl)

print(str(len(in_appl.index)) + " - Every " +
      str(get_time_interval(in_appl)) + " seconds")

fill_with_avgs(stocks)
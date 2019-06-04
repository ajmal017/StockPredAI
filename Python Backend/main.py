# -*- coding: utf-8 -*-
from my_utils import *

print("Appending datasets...")
amzn = join_datasets(r'datasets/stock/AMZN_1MIN_ze7avh/*.csv')
# 9:30 to 15:59

spx = join_datasets(r'datasets/index/SPX_1MIN_8v96zt/*.csv')
# 9:30 to 15:59

usd_eur = join_datasets(r'datasets/forex/EURUSD_5MIN_99rasp/*.csv')
# all the time every 5

print("Formating dates...")
format_dates(amzn)
format_dates(spx)
format_dates(usd_eur)

print("Intersecting datasets...")
initial_date = find_common_biggest_initial_date([amzn, spx, usd_eur])
final_date = find_common_smallest_final_date([amzn, spx, usd_eur])

amzn = crop_dataset_from_dates(amzn, initial_date, final_date)
spx = crop_dataset_from_dates(spx, initial_date, final_date)
usd_eur = crop_dataset_from_dates(usd_eur, initial_date, final_date)

print(amzn)
print(spx)
print(usd_eur)

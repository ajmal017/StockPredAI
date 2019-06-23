# -*- coding: utf-8 -*-
import pandas as pd
import glob
import sys


def join_datasets(path):
    all_files = sorted(glob.glob(path))

    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=None)
        li.append(df)
    return pd.concat(li, axis=0, ignore_index=True)


def format_single_date(date):
    if (date.find(":") != -1):
        formatted = date.replace(":", "").replace(
            ".", "").replace(" ", "").replace("-", "")
        return int(formatted)/100
    else:
        print("returning: ")
        print(date)
        return int(date)/100


def format_dates(df):
    df[0] = pd.Series([format_single_date(date)
                       for date in df[0]], index=df.index)


def find_common_biggest_initial_date(dfs):
    common_date = 0
    for df in dfs:
        date = df.iloc[0][0]
        if common_date < date:
            common_date = date
    return common_date


def find_common_smallest_final_date(dfs):
    common_date = sys.maxsize
    for df in dfs:
        date = df.iloc[len(df.index)-1][0]
        if common_date > date:
            common_date = date
    return common_date


def crop_dataset_from_dates(df, initial_date, final_date):
    cropped_df = df[df[0] >= initial_date]
    return cropped_df[cropped_df[0] <= final_date]


def get_time_interval(df):
    return df.iloc[1][0] - df.iloc[0][0]

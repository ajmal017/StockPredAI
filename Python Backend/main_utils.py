# -*- coding: utf-8 -*-
import glob
import sys

import pandas as pd


def join_datasets(path, with_rows):
    all_files = sorted(glob.glob(path))

    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=None)
        df = df[with_rows]
        li.append(df)
    return pd.concat(li, axis=0, ignore_index=True)


def format_single_date(date):
    if (date.find(":") != -1):
        formatted = date.replace(":", "").replace(
            ".", "").replace(" ", "").replace("-", "")
        return int(formatted) / 100
    else:
        return int(date) / 100


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
        date = df.iloc[len(df.index) - 1][0]
        if common_date > date:
            common_date = date
    return common_date


def validate_date_frontiers(dfs):
    common_start = dfs[0][0][0]
    for i in range(1, len(dfs)):
        current = dfs[i][0][0]
        if current != common_start:
            return False

    last = dfs[0][0]
    common_end = last[len(last) - 1]
    for i in range(1, len(dfs)):
        current = dfs[i][0][len(dfs[i][0]) - 1]
        if current != common_end:
            return False

    return True


def crop_dataset_to_frontiers(dfs):
    while not validate_date_frontiers(dfs):

        common_first = find_common_biggest_initial_date(dfs)
        common_last = find_common_smallest_final_date(dfs)

        for i in range(len(dfs)):
            dfs[i] = dfs[i][dfs[i][0] >= common_first]
            dfs[i] = dfs[i][dfs[i][0] <= common_last]
            dfs[i] = dfs[i].reset_index(drop=True)


def get_time_interval(df):
    return df.iloc[1][0] - df.iloc[0][0]

import sys


def fill_with_avgs(dfs):
    end_index = 0

    for df in dfs:
        if end_index < len(df[0]):
            end_index = len(df[0])

    i = 0
    while i < end_index:
        i += 1
        row = []
        for j in range(0, len(dfs)):
            row.append(dfs[j][0][i])

        min_in_row = min(row)
        for j in range(0, len(dfs)):
            if row[j] > min_in_row:
                # if this value is not in another row
                print("found missing value: ", row, "at index: ", i)

                dfs[j].append([min_in_row, 0, 0, 0, 0, 0])
                row[j] = min_in_row

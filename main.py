import pandas as pd
from pandas import json_normalize

df = pd.read_json("companies.json")

columns = []

columns.append(df.columns[0])

for i, row in df.itertuples():
    # print(row.index)
    # print(row.name)

    print(row["name"])
    print(row["departments"])
    # print(row["name"], row["departments"])

df.to_csv("courses.csv")

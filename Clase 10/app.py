
import pandas as pd

df = pd.read_csv("productos.csv")
print(df)

with open("productos.csv", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        print(row)


import os
import pandas as pd
import tabulate

CSV_PATH = os.path.join('dctechnology.csv')
CSV_PATH = CSV_PATH.encode('utf-8').strip()

df = pd.read_csv(CSV_PATH)

print(df)

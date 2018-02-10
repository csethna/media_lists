import os
import pandas as pd
import tabulate as tb

CSV_PATH = os.path.join('dctechnology.csv')
# CSV_PATH = CSV_PATH.encode('utf-8').strip()

cols = ["first", "last", "outlet", "title", "contact"]

df = pd.read_csv(CSV_PATH, names=cols, engine='python')

print(df)

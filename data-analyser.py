import pandas as pd
from tabula import wrapper
import numpy as np


path = '/Users/shivahs/Documents/IRS/stash/USHI/go-auth-test/thrifty/final.csv'

names = ['Date', 'Transaction Description', 'Amount']
df = pd.read_csv(path, names=names, header=None)

df['Date-New']=pd.to_datetime(df.Date, format='%d/%m/%Y')

df.sort_values(by='Date-New', ascending=True, inplace=True)

del df['Date']

df = df.reset_index(drop=True)


print(df[nov_mask])


import pandas as pd
from tabula import wrapper
import numpy as np
import csv
import re
import os

path = '/Users/shivahs/Documents/IRS/stash/USHI/go-auth-test/thrifty/statements/'

files = [f for f in os.listdir(path)]
files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)

for i, file in enumerate(files):
    filePath = path + file
    print(filePath)

    wrapper.convert_into(filePath, "output"+ str(i) +".csv", output_format="csv", pages='all')

    names = ['Date', 'Transaction Description', 'test1', 'Amount', 'test2']
    df1 = pd.read_csv("output"+ str(i) +".csv", names=names, header=None)

    del df1['test1']
    del df1['test2']

    df1 = df1[pd.notnull(df1['Date'])]
    df1 = df1[pd.notnull(df1['Transaction Description'])]
    df1 = df1[pd.notnull(df1['Amount'])]

    patternDel = "(\d+/\d+/\d)"
    filter = df1['Date'].str.contains(patternDel)
    df1 = df1[filter]
    df1.to_csv('semi-final.csv', mode='a', index=False, header=False, )

    os.remove("output"+ str(i) +".csv")

names2 = ['Date', 'Transaction Description', 'Amount']
df2 = pd.read_csv("semi-final.csv", names=names2, header=None)

df2['Date-New']=pd.to_datetime(df2.Date, format='%d/%m/%Y')
df2.sort_values(by='Date-New', ascending=True, inplace=True)
del df2['Date']

df2 = df2.reset_index(drop=True)

print(df2[df2.Amount.str.contains('Cr')])
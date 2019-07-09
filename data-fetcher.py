import pandas as pd
from tabula import wrapper
import numpy as np
import csv
import re
import os

path = 'statements/'

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

names2 = ['Date', 'TransactionDescription', 'TransactionAmount']
df2 = pd.read_csv("semi-final.csv", names=names2, header=None)

df2['TransactionDate']=pd.to_datetime(df2.Date, format='%d/%m/%Y')
df2.sort_values(by='TransactionDate', ascending=True, inplace=True)
del df2['Date']

df2 = df2.reset_index(drop=True)

df2['TransactionType'] = ["Credit" if x == True else "Debit" for x in df2.TransactionAmount.str.contains('Cr')]
df2.TransactionAmount = [col.replace(' Cr', '') for col in df2.TransactionAmount]
df2["TransactionAmount"] = df2["TransactionAmount"].str.replace(",","").astype(float)
df2["TransactionAmount"] = pd.to_numeric(df2["TransactionAmount"])

df2.to_csv('txn-dataset.csv', mode='a', index=False, header=False, )

os.remove("semi-final.csv")

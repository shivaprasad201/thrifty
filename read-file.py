import pandas as pd
from tabula import wrapper
import numpy as np
import csv
import re
import os

path = '/Users/shiva/Downloads/'

files = [f for f in os.listdir(path)]
files = filter(lambda f: f.endswith(('.pdf','.PDF')), files)

for i, file in enumerate(files):
    filePath = path + file
    print(filePath)

    wrapper.convert_into(filePath, "output"+ str(i) +".csv", output_format="csv", pages='all')

    names = ['Date', 'Transaction Description', 'test1', 'Amount', 'test2']
    df = pd.read_csv("output"+ str(i) +".csv", names=names, header=None)

    del df['test1']
    del df['test2']

    df = df[pd.notnull(df['Date'])]
    df = df[pd.notnull(df['Transaction Description'])]
    df = df[pd.notnull(df['Amount'])]

    patternDel = "(\d+/\d+/\d)"
    filter = df['Date'].str.contains(patternDel)
    df = df[filter]
    df.to_csv('final.csv', mode='a', header=False, )
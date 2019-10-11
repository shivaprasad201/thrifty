import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from pandas.plotting import scatter_matrix


rcParams['figure.figsize'] = 15, 6

path = 'txn-dataset.csv'

names = ['TransactionDescription', 'TransactionAmount','TransactionDate', 'TransactionType' ]

df = pd.read_csv(path, names=names, header=None, parse_dates=['TransactionDate'], index_col='TransactionDate')

# df.plot()
# plt.subplot()
# df.plot.pie(subplots=True)
# scatter_matrix(df)
# df.hist()

ts = df['TransactionAmount'] 
ts.plot()
# ts.hist()

ts_log = np.log(ts)
ts_log.plot()
# ts_log.hist()

plt.show()

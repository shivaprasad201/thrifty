# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# Load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
url = "/Users/shiva/Downloads/car.data"
names = ['price-range', 'maintenance', 'seating-capacity', 'scratches-and-dents', 'boot-capacity', 'kilometers-run', 'condition']
dataset = pandas.read_csv(url, names=names)


# Visualizing plots

# # shape
# print(dataset.shape)

# head
# print(dataset.head(20))

# descriptions
# print(dataset.describe())

# class distribution
# print(dataset.groupby('condition').size())

# box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()

# # histograms
# dataset.hist()
# plt.show()
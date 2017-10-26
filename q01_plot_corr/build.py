# %load q01_plot_corr/build.py
# Default imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap

data = pd.read_csv('data/house_prices_multivariate.csv')

#data.info()
# Write your solution here:

def plot_corr(df, size=11):
    #dataPlot = sns.load_dataset(df)
    cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
    sns.pairplot(df[cols])
    plt.figsize(12,12)
    plt.set_cmap('YlOrRd')
    #plt.subplots(figsize=(50,100))
    plt.show()

#plot_corr(data)

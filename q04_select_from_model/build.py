# %load q04_select_from_model/build.py
# Default imports
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
import pandas as pd
import numpy as np

data = pd.read_csv('data/house_prices_multivariate.csv')
np.random.seed(9)
def select_from_model (df):
    X = df.iloc[:,:-1]
    #print(X)
    Y = df['SalePrice']
    model = RandomForestClassifier()
    rfe = SelectFromModel(model)
    fit = rfe.fit(X, Y)
    #print("Num Features: %d") % fit.n_features_
    return X.columns.values[fit.get_support()].tolist()
    #print("Selected Features: %s") % fit.support_
    #print("Feature Ranking: %s") % fit.ranking_

# Your solution code here
#select_from_model(data)
#print(type(a))

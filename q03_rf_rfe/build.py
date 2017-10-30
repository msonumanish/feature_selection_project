# %load q03_rf_rfe/build.py
# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# Your solution code here

def rf_rfe(df):
    X = df.iloc[:,:-1]
    #print(X)
    Y = df['SalePrice']
    model = RandomForestClassifier()
    rfe = RFE(model, n_features_to_select=17)
    fit = rfe.fit(X, Y)
    #print("Num Features: %d") % fit.n_features_
    return X.columns.values[fit.support_].tolist()
    #print("Selected Features: %s") % fit.support_
    #print("Feature Ranking: %s") % fit.ranking_

#l=rf_rfe(data)
#print(type(l))

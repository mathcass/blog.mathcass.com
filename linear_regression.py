# Here's a brief attempt at recreating linear regression via statsmodels and two
# ways via numpy

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# read data into a DataFrame
data = pd.read_csv(
    'http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
lm = smf.ols(formula='sales ~ TV', data=data).fit()
print(lm.params)


y = data.sales.values
X = np.array([data.TV.values, np.ones(data.shape[0])])
X = X.T

params, resid, rank, S = np.linalg.lstsq(X, y)
print(params)

print(np.linalg.pinv(X).dot(y))

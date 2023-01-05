import pyesg
import numpy as np
from pyesg import NelsonSiegelInterpolator, SvenssonInterpolator
from pyesg.datasets import load_ust_historical

# load a dataset of historical US Treasury rates, contained in pyesg.datasets
# ust is a pandas dataframe of rates for various maturities, indexed by year and month
ust = load_ust_historical()

# we will be interpolating rates from the file:
# y - the observed US Treasury rate for the given maturity for a select observation date
# X - the maturity of the bond measured in years
y = ust.iloc[-10].values
X = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30])

# create Nelson-Siegel and Nelson-Siegel-Svensson interpolator objects
# then fit both models using the historical data
nelson_siegel = pyesg.NelsonSiegelInterpolator()
svensson = pyesg.SvenssonInterpolator()
nelson_siegel.fit(X, y)
svensson.fit(X, y)

# predict values for each maturity from 1 to 30 years
nelson_siegel.predict(np.arange(1, 31, 1))
# array([0.02033871, 0.02252733, 0.02403659, 0.02510373, 0.02587762,
#        0.02645304, 0.02689131, 0.02723275, 0.02750438, 0.02772458,
#        0.02790617, 0.02805818, 0.02818715, 0.02829786, 0.0283939 ,
#        0.02847798, 0.02855218, 0.02861815, 0.02867718, 0.02873031,
#        0.02877839, 0.02882209, 0.02886199, 0.02889857, 0.02893222,
#        0.02896329, 0.02899205, 0.02901876, 0.02904362, 0.02906683])
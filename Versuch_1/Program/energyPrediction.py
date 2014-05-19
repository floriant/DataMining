import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as slp
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch
import sklearn.feature_selection as fs
import sklearn.svm as svm
import sklearn.cross_validation as cval
import sklearn.metrics as metrics

df = pd.read_csv("../res/EnergyMixGeo.csv")

#storing dataframe data into variables
energyDataIn = df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']]
energyDataOut = df['CO2Emm']

#generating SVR for learning, C and epsilon need to be optimized!
#svr = svm.SVR(kernel="linear", C=1.0, epsilon=0.1)
svr = svm.SVR(kernel="linear", C=5.0, epsilon=0.10789)

#creating n=10 crossvalidation, results are scores
crossval = cval.cross_val_score(svr, energyDataIn, energyDataOut, cv=10, scoring=metrics.mean_squared_error)
#printing the results with calculation according to script
print "##### Cross Validation Results #####"
print crossval
print "Cross Validation Score: %0.3f (+/- %0.3f)" % (crossval.mean(), crossval.std() / 2)
print ""

#fitting data on svr, this is the training process
trained = svr.fit(energyDataIn, energyDataOut)
prediction = trained.predict(energyDataIn)
print "##### Predicted Data #####"
print prediction
print ""

# getting mean absolute deviation (MAD) according to method from script
mad = 1.0/len(df)*np.sum(np.abs(prediction-energyDataOut))
print "##### Mean Absolute Difference #####"
print "Mean Absolute Difference 1 \t %2.3f" % (mad)

#plotting from output and prediction
plt.subplot(211)
plt.plot(np.arange(len(df)), prediction, 'r')
plt.subplot(212)
plt.plot(np.arange(len(df)), energyDataOut, 'k')
plt.show()


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

energyIn = df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']]
energyOut = df['CO2Emm']
print energyOut.tolist()
#print energyIn.values

svr = svm.SVR(kernel="linear")
crossval = cval.cross_val_score(svr, energyIn, energyOut, cv=10, score_func=metrics.mean_squared_error)
print crossval



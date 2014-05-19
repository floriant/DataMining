import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as slp
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch
import sklearn.feature_selection as fs

df = pd.read_csv("../res/EnergyMixGeo.csv")
featureSelector = fs.SelectKBest(score_func=fs.f_regression,k="all")

featureSelector.fit(df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']],df.loc[:,["CO2Emm"]])

print featureSelector.scores_
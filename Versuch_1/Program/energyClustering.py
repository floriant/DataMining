#################################################
########### WORK IN PROGRESS ####################
#################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as slp
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch

df = pd.read_csv("../res/EnergyMix.csv")
print df
print df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']]

X = slp.scale(df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']], with_mean=False)
print "-------------------------"
print X

Y = ssd.pdist(X, metric="correlation")
Z = sch.linkage(Y)
#print df.loc[:,'Country']
labeling = []
key = 1
for label in df['Country']:
    labeling.append(label)
    key = key + 1
print labeling
sch.dendrogram(Z, labels=labeling, orientation="left")

D = sch.fcluster(Z,0.0)
print "----------"
print D
#plt.plot()
plt.show()



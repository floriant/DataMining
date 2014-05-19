#################################################
########### WORK IN PROGRESS ####################
#################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as slp
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch

df = pd.read_csv("../res/EnergyMixGeo.csv")
print df
print df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']]

X = slp.scale(df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']], with_mean=False)
print "-------------------------"
print X

Y = ssd.pdist(X, metric="correlation")
Z = sch.linkage(Y, method="average")
#print df.loc[:,'Country']
labeling = []
key = 1
for label in df['Country']:
    labeling.append(label)
    key = key + 1
print labeling
plt.figure(1)
sch.dendrogram(Z, labels=labeling, orientation="left")
D = sch.fcluster(Z,4, criterion="maxclust")
print "----------------------"
print D

df['Cluster'] = D
print df
df.to_csv("../res/EnergyMixGeoCluster.csv")
#print df[df['Cluster'].isin([1])]
print "##################################################"
#df1 = df[df['Cluster'].isin([1])].stack()
#print df.ix[df['Cluster']==1, 'Oil','Gas','Coal','Nuclear','Hydro']
print df[df['Cluster'].isin([1])]
plt.figure(2)
for index, cluster in df[df['Cluster'].isin([1])].iterrows():
    print cluster
    plt.subplot(411)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 0")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

for index, cluster in df[df['Cluster'].isin([2])].iterrows():
    print cluster
    plt.subplot(412)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 1")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

for index, cluster in df[df['Cluster'].isin([3])].iterrows():
    print cluster
    plt.subplot(413)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 2")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

for index, cluster in df[df['Cluster'].isin([4])].iterrows():
    print cluster
    plt.subplot(414)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 3")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

plt.show()
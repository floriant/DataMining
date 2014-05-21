#################################################
########### WORK IN PROGRESS ####################
#################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as slp
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as sch

# Reading CSV
df = pd.read_csv("../res/EnergyMixGeo.csv")

# Standardizig /scale), Distance Calculation (pdist) and hierarchical Clustering (linkage)
X = slp.scale(df.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']], with_mean=False)
print X
Y = ssd.pdist(X, metric="correlation")
Z = sch.linkage(Y, method="average")

# Generating Figure 1 (dendogram)
labeling = []
key = 1
for label in df['Country']:
    labeling.append(label)
    key = key + 1
plt.figure(1)
sch.dendrogram(Z, labels=labeling, orientation="left")
D = sch.fcluster(Z,4, criterion="maxclust")
print "##### Clustering Values #####"
print D
print ""

# Saving Data to CSV with Cluster Value assigned to each Variable
df['Cluster'] = D
df.to_csv("../res/EnergyMixGeo.csv")

# Generating Figure 2 (individual Clusters)
plt.figure(2)
for index, cluster in df[df['Cluster'].isin([1])].iterrows():
    plt.subplot(411)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 0")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

for index, cluster in df[df['Cluster'].isin([2])].iterrows():
    plt.subplot(412)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 1")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

for index, cluster in df[df['Cluster'].isin([3])].iterrows():
    plt.subplot(413)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 2")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

for index, cluster in df[df['Cluster'].isin([4])].iterrows():
    plt.subplot(414)
    r = range(2,7,1)
    plt.plot(r, cluster[r], hold=True)
    plt.title("cluster 3")
    plt.xticks(r,['Oil','Gas','Coal','Nuclear','Hydro'])

plt.show()
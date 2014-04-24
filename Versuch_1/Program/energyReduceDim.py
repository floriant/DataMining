import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap


resourceFolder = '../res/'

dataframe = pd.read_csv(resourceFolder + 'EnergyMix.csv')

df = dataframe.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']]

print df

imap = Isomap()
df_reduced = imap.fit_transform(df)
print df_reduced

plt.plot(df_reduced[:,0],df_reduced[:,1],'.')
for index, country in enumerate(dataframe["Country"]):
        plt.text(df_reduced[index,0], df_reduced[index,1], country)

plt.savefig('../doc/EnergyMix_Reduced.png')
plt.show()
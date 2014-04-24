import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



resourceFolder = '../res/'




#if __name__ == '__main__':
dataframe = pd.read_csv(resourceFolder + 'EnergyMix.csv')

df = dataframe.loc[:,['Oil','Gas','Coal','Nuclear','Hydro']]

print df

df.to_csv(resourceFolder + 'EnergyMixOnlyResources.csv')
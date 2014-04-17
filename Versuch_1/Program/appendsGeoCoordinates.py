import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("../res/EnergyMix.csv")

range = df.index
#print df

plt.barh(range + 0, df['Oil'], 0.15, color='r')
plt.barh(range + 0.2, df['Gas'], 0.15, color='g')
plt.barh(range + 0.4, df['Coal'], 0.15, color='b')
plt.barh(range + 0.6, df['Nuclear'], 0.15, color='#ff00ff')
plt.barh(range + 0.8, df['Hydro'], 0.15, color='#ffff00' )

plt.yticks(range, df['Country'])
plt.xlabel('Verbrauch')
plt.grid(True)

#todo: legende mit Farben
#todo: bild in schöner größe plotten

#plt.savefig('perf.png')
plt.show()
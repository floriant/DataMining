import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib
import json
import time

resourceFolder = '../res/'


def plot_energy_mix(dataframe, show=False):
    energySources = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
    range = dataframe.index

    fig = plt.figure(figsize=(20, 90))
    #mit logarithmischer Skala werden die Balken nicht richtig geplottet
    #plt.semilogx(range, np.sin(2*np.pi*range))
    b1 = plt.barh(range + 0, dataframe['Oil'], 0.13, color='#ff0000')
    b2 = plt.barh(range + 0.16, dataframe['Gas'], 0.13, color='#009999')
    b3 = plt.barh(range + 0.34, dataframe['Coal'], 0.13, color='#0000ff')
    b4 = plt.barh(range + 0.52, dataframe['Nuclear'], 0.13, color='#ff00ff')
    b5 = plt.barh(range + 0.70, dataframe['Hydro'], 0.13, color='#ffff00' )


    plt.yticks(range + 0.4, dataframe['Country'])
    plt.xlabel('Energy consumption by resource')
    plt.grid(True)

    #plt.autoscale()

    plt.legend([b1, b2, b3, b4, b5], energySources)

    plt.savefig(resourceFolder + 'EnergyMix.png', dpi=72)#, transparent=True)
    plt.savefig(resourceFolder + 'EnergyMix_transparent.png', dpi=72, transparent=True)
    plt.savefig(resourceFolder + 'EnergyMix.pdf', transparent=True)

    plt.show()
    plt.clf() #clear figure



def append_geo_coordinates(dataframe):
    #source: http://stackoverflow.com/questions/18807114/http-error-403-with-api-id-in-accessing-google-maps
    countries = dataframe["Country"]
    lat = []
    long = []

    #Loop to feed the func with adresses and output the lat & lng.
    for c in countries:
        r = geocode(c)
        print "%s -> %s : %s" % (c, r['lat'], r['lng'])
        lat.append(r['lat'])
        long.append(r['lng'])
        time.sleep(0.7) #damit man nicht von google gesperrt wird

    #add columns for latitude and longitude
    dataframe['Lat'] = lat
    dataframe['Long'] = long

    return dataframe #eigentlich unnoetig, aber vielleicht kann mans mal brauchen


def geocode(addr):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % (urllib.quote(addr.replace(' ', '+')))
    data = urllib.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")
    #A little ugly I concede, but I am open to all advices :) '''
    return info



if __name__ == '__main__':
    dataframe = pd.read_csv(resourceFolder + 'EnergyMix.csv')
    #print df

    plot_energy_mix(dataframe, show=False)

    append_geo_coordinates(dataframe)

    dataframe.to_csv(resourceFolder + 'EnergyMixGeo.csv')
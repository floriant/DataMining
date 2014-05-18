# -*- coding:utf8 -*-
import pandas as pd


class GoogleMap:
    import pymaps as pm

    def __init__(self):
        self.pymapsInstance = self.pm.PyMap()
        self.__initializeIcons()
        self.pymapsInstance.key = "ABQIAAAAQQRAsOk3uqvy3Hwwo4CclBTrVPfEE8Ms0qPwyRfPn-DOTlpaLBTvTHRCdf2V6KbzW7PZFYLT8wFD0A"  # you will get your own key
        self.pymapsInstance.maps[0].zoom = 2

    def __initializeIcons(self):
        self.icons = []

        #jede Farbe wird einem Cluster zugeordnet
        colors = ("blue", "green", "yellow", "red")  #TODO: Ob Farben existieren ist nicht getestet
        for index, color in enumerate(colors):
            icon = self.pm.Icon('icon%d' % index)
            icon.image = "http://labs.google.com/ridefinder/images/mm_20_" + color + ".png"  # for testing only!
            icon.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"  # do not hotlink from your web page!

            self.icons.append(icon)
            self.pymapsInstance.addicon(icon)


    def addClusteredEnergyMix(self, df):
        def energyMixToString(data):
            return "<b>%s</b> Total in 2009: %s<br/>Oil: %s Gas: %s Coal: %s Nuclear: %s Hydro: %s" % \
                   (data["Country"], data["Total2009"], data["Oil"], data["Gas"], data["Coal"], data["Nuclear"],
                    data["Hydro"])

        #TODO: über zeilen iterieren
        for i in df.index:
            row = df.iloc[i]
            #es gibt 4 cluster
            icon = row["Cluster"]  #TODO: Cluster-Nummer auf icon umbauen
            icon = 'icon%s' % (icon - 1)
            caption = energyMixToString(row)
            point = [row["Lat"], row["Long"], caption, icon]

            self.pymapsInstance.maps[0].setpoint(point)


    def saveToFile(self, filename):
        open(filename, 'wb').write(self.pymapsInstance.showhtml())  # generate test file


if __name__ == "__main__":
    df = pd.read_csv("../res/EnergyMixGeoCluster.csv")

    outputMap = GoogleMap()
    outputMap.addClusteredEnergyMix(df)
    outputMap.saveToFile('../doc/EnergyMix2009.html')
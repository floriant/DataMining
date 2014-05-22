import pylast as pl
import numpy as np
import pprint as pp

# instantiate network
network = pl.get_lastfm_network()

# get Band
band = network.get_artist("J.B.O")

topfans = band.get_top_fans(10)

group=[a.item for a in topfans]

print band
print topfans
print group


# need to be done as function in recommendations.py
userDict = {}
allBands = []
for user in group:
    userDict[user] = {}
    #userObject = network.get_user(user)
    #print userObject.name
    topArtists = user.get_top_artists()[0:20]
    for i,artist in enumerate(topArtists):
        bandFlag = 0
        for band in allBands:
            if(topArtists[i].item.name == band):
                bandFlag = 1
        if(bandFlag == 0):
            allBands.append(topArtists[i].item.name)
print allBands
for user in group:
    for band in allBands:
        userDict[user][band] = 0
    for i,artist in enumerate(topArtists):
        userDict[user][topArtists[i].item.name] = 1

pp.pprint(userDict)
print userDict
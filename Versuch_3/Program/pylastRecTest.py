import pylast as pl
import numpy as np
import pprint as pp
import recommendations as recom
import recommtest1 as rct

# instantiate network
network = pl.get_lastfm_network()

# get Band
band = network.get_artist("J.B.O")

topfans = band.get_top_fans(10)

group=[a.item for a in topfans]

#print band
#print topfans
#print group

userDict = recom.createLastfmUserDict(group)
pp.pprint(userDict)
selectedUser = group[3]
print selectedUser
result = rct.topMatches(userDict, group[3].get_name(), recom.sim_euclid)
pp.pprint(result)


#print result[0][1].key()
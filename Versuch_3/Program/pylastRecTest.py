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
selectedUser = group[1].get_name()
print "Selected User: "
pp.pprint(selectedUser)
print "===================================="
topMatches = recom.topMatches(userDict, group[1].get_name(), recom.sim_euclid)
print "Top Matches: "
pp.pprint(topMatches)
print "===================================="
recommendations = recom.getRecommendations(userDict, group[1].get_name(), recom.sim_euclid)
print "Recommendations: "
pp.pprint(recommendations)
print "===================================="


#print result[0][1].key()
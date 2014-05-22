# -*- coding: utf-8 -*-
import recommendations as reco
import numpy as np


def topMatches(prefs,person,similarity):
    critic_similarities = {}
    
   
    result = []
    for critic in prefs.iterkeys() :
        
        if critic != person:
            index = 0
            sim = abs(similarity(prefs, person, critic))
            if len(result) == 0:
                result.append([critic, sim])
            else:
                for i, value in enumerate(result):
                    if value[1] < sim:
                        index = i+1
                    else:
                        break
                result.insert(index,[critic, sim])

    #print result
    return result

if __name__ == "__main__":
    for testperson in critics.iterkeys() :
        print "#" *60
        print "Euclid for", testperson
        tMatch = topMatches(critics,testperson,reco.sim_euclid)
        for m in tMatch :
            print m[0], m[1]
        print "-" *20    
        print "Pearson for", testperson 
        tMatch = topMatches(critics,testperson,reco.sim_pearson)
        for m in tMatch :
            print m[0], m[1]


# -*- coding: utf-8 -*-
import recommendations as reco
import numpy as np

##############################################################
#2.2 calculate similarities
##############################################################

def run_assignment_2_2():
    print "-"*50, "\n", "assignment 2.2: Calculate similarites\n", "-"*50

    for testperson in critics.iterkeys():
        print "Euclidean Distances for", testperson
        tMatch = reco.topMatches(critics, testperson, reco.sim_euclid)
        for m in tMatch :
            print "  ", m[0], m[1]
        print "-" *20
        print "Pearson Distances for", testperson
        tMatch = reco.topMatches(critics, testperson, reco.sim_pearson)
        for m in tMatch :
            print "  ", m[0], m[1]

    print "-"*50

##############################################################
#2.3 UCF
##############################################################


def run_assignment_2_3():
    print "-"*50, "\n", "assignment 2.3: User based collaborative filtering (UCF)\n", "-"*50

    pass

    print "-"*50

##############################################################
#2.4 ICF
##############################################################



def run_assignment_2_4():
    print "-"*50, "\n", "assignment 2.4: Item based collaborative filtering (ICF)\n", "-"*50
    transCritics = reco.transformCritics(critics)
    person = 'Toby'

    recommendations_euclid = getRecommendedItems(transCritics, person, reco.sim_euclid)
    print "Recommendations for %s (calculated with Euclidean Distance):\n " % (person), recommendations_euclid

    recommendations_pearson = getRecommendedItems(transCritics, person, reco.sim_pearson)
    print "Recommendations for %s (calculated with Pearson Distance):\n " % (person), recommendations_pearson

    print "-"*50



if __name__ == "__main__":
    critics = reco.critics;

    #TODO uncomment all assignments when done
    run_assignment_2_2()
    run_assignment_2_3()
    run_assignment_2_4()



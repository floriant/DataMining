# -*- coding: utf-8 -*-
import recommendations as reco
import numpy as np

##############################################################
#2.2 calculate similarities
##############################################################
def topMatches(prefs, person, similarity):
    critic_similarities = {}
   
    result = []
    for critic in prefs.iterkeys():
        
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
                result.insert(index, [critic, sim])

    #print result
    return result


def run_assignment_2_2():
    print "-"*50, "\n", "assignment 2.2: Calculate similarites\n", "-"*50

    for testperson in critics.iterkeys():
        print "Euclidean Distances for", testperson
        tMatch = topMatches(critics, testperson, reco.sim_euclid)
        for m in tMatch :
            print "  ", m[0], m[1]
        print "-" *20
        print "Pearson Distances for", testperson
        tMatch = topMatches(critics, testperson, reco.sim_pearson)
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

def transformCritics(critics):
    movies = {}

    for critic, details in critics.iteritems():
        #details is a dictionary with movie titles as keys and the critic's ratings as values
        for title, rating in details.iteritems():
            #assert that the dictionary for this movie exists
            if title not in movies:
                movies[title] = {}
            movies[title][critic] = rating

    return movies


def calculateSimilarItems(prefs, similarity):
    similarItems = {}

    for title in prefs:
        similarItems[title] = topMatches(prefs, title, similarity)

    return similarItems


def getRecommendedItems(prefs, person, similarity):
    similarItems = calculateSimilarItems(prefs, similarity)
    result = []

    unknownMovies = []
    for movie in similarItems:
        if movie not in critics[person]:
            unknownMovies.append(movie)

    #print "unknownMovies: ", unknownMovies, "\n", "-"*15


    for unknownMovie in unknownMovies:
        sumRecommendations = 0
        sumSimilarities = 0

        for ratedMovie, rating in critics[person].iteritems():
            for item in similarItems[unknownMovie]:
                # item is an arrray [title, similarityToUnknownMovie]
                if item[0] == ratedMovie:
                    if item[1] > 0: #if pearson distance was used similarities < 0 should be ignored
                        sumSimilarities += item[1]
                        sumRecommendations += rating * item[1]

        # if pearson was used, sumSimilarities might equal 0
        recommendation = sumRecommendations / sumSimilarities if sumSimilarities != 0 else 0

        #print "recommendation for movie '%s' = %f" % (unknownMovie, recommendation)

        #insert weighted recommendation into sorted result array
        if len(result) == 0:
            result.append([unknownMovie, recommendation])
        else:
            index = 0
            for i, value in enumerate(result):
                if value[1] > recommendation:
                    index = i+1
                else:
                    break
            result.insert(index, [unknownMovie, recommendation])

    return result


def run_assignment_2_4():
    print "-"*50, "\n", "assignment 2.4: Item based collaborative filtering (ICF)\n", "-"*50
    transCritics = transformCritics(critics)
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



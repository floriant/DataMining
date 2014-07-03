# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 20:24:29 2014

"""
import pprint as pp

import newsfeatures21 as nf21
import newsfeatures221 as nf221
import newsfeatured222_2 as nf222
import newsfeatures224 as nf224

def scrape_feedlist(load_from_disk=True):
    return nf21.scrape_feedlist(load_from_disk)


def getarticlewords():
    return nf221.getarticlewords()


def makematrix(allw, articlew):
    nf222.makematrix(allw, articlew)
    return (nf222.wordvec, nf222.wordInArt)


def nnmf(A, m, it):
    return nf224.nnmf(A, m, it)

if __name__ == "__main__":    
    allwords, articlewords, articletitles = getarticlewords()
    
    artWordsDict = {} 
    for i in range(len(articletitles)):
        artWordsDict[i] = articlewords[i]
    #pp.pprint(artWordsDict)
    A = makematrix(allwords, artWordsDict)    
    
    #result = makematrix(allwords, articlewords)
    #wordVec, wordInArt = result
    
    # Test input here:
    #pp.pprint(allwords)
    pp.pprint(articlewords)
    #art = 2;
    #pp.pprint(articlewords[art])
    #pp.pprint(articletitles[art])
    
    #pp.pprint(wordVec)
    #pp.pprint(wirdInArt)
    
    #
    #artWordsDict = {} 
    #for article in articlewords :
    #    artWordsDict[article] = articlewords[article]
    #pp.pprint(artWordsDict)
    #A = makematrix(allwords, artWordsDict)
    #pp.pprint(A)
    
    m = 3
    it = 2
    #result = nnmf(A, m, it)
    #W, H = result
    #pp.pprin(W)
    #pp.pprint(H)    
    

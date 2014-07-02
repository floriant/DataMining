# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np

#import newsfeatures_dummy as nf
import newsfeatures as nf


#2.1
allfeeds = nf.scrape_feedlist(load_from_disk=True)
print 'printing loaded feeds:'
for key, value in allfeeds.items():
    print key, ": ", value

print "\n", "-" * 64, "\n"



#2.2.1
#TODO use named tuples instead of tuples
allwords, articlewords, articletitles = nf.getarticlewords()

print "allwords:\n", allwords, "\narticlewords:\n", articlewords, "articletitles:", articletitles

#2.2.2
result = nf.makematrix(allwords, articlewords, articletitles)
wordVec, wordInArt, articletitles = result
print "wordVe:\n", wordVec, "\nwordInArt:\n", wordInArt, "articletitles:\n", articletitles

"""
#2.2.3
awMatrix = nf.transformMatrix(wordInArt)

#2.2.4
result = nf.nnmf(awMatrix, 7, 10)
W, H = result

#2.3
"""
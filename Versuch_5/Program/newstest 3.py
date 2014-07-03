# -*- coding: utf-8 -*-

#import newsfeatures_dummy as nf
import newsfeatures231_1 as nf

import pprint as pp


#2.1
allfeeds = nf.scrape_feedlist(load_from_disk=True)
'''
print 'printing loaded feeds:'
for key, value in allfeeds.items():
    print key, ": ", value

print "\n", "-" * 64, "\n"
'''


#2.2.1
#TODO use named tuples instead of tuples
allwords, articlewords, articletitles = nf.getarticlewords()

#print "allwords:\n", allwords, "\narticlewords:\n", articlewords, "articletitles:", articletitles

#2.2.2
result = nf.makematrix(allwords, articlewords, articletitles)
wordVec, wordInArt, articletitles = result
#print "wordVe:\n", wordVec, "\nwordInArt:\n", wordInArt

#2.2.3
awMatrix = nf.transformMatrix(wordInArt)

#2.2.4
result = nf.nnmf(awMatrix, 7, 10)
W, H = result
#2.3
ImportantM = nf.importantM(H, wordVec)
pp.pprint(ImportantM)
"""
###exampledata
allwords = {'aided':3, 'actionfor': 3, 'ambitionsthe':2, 'reboot':4, 'four':8, 'accused': 10, 'into': 3, 'racism': 4, 'debate':3}
articlewords = {}
articlewords[0] = {'accused': 1, 'into': 1, 'racism': 2, 'debate': 1}
articlewords[1] = {'accused': 1, 'aided': 1, 'actionfor': 2, 'ambitionsthe': 1, 'reboot': 1, 'four': 2}
articlewords[2] = {'aided':1, 'ambitionsthe':1, 'reboot':1, 'four':2, 'into': 1, 'debate':1}
articlewords[3] = { 'reboot':1, 'four':2, 'accused': 2}
articlewords[4] = {'aided':1, 'actionfor': 1, 'ambitionsthe':1, 'reboot':1, 'four':2, 'accused': 2, 'into': 1, 'racism': 2, 'debate':1}
articlewords[5] = {'actionfor': 1}

print "-"*64
print "-"*64
print "allwords:\n", allwords
print "articlewords:\n", articlewords

"""
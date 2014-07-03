# -*- coding: utf-8 -*-
import pprint as pp

#import newsfeatures_dummy as nf
import newsfeatures as nf


#2.1
allfeeds = nf.scrape_feedlist(load_from_disk=True)
'''
print 'printing loaded feeds:'
for key, value in allfeeds.items():
    print key, ": ", value

print "\n", "-" * 64, "\n"
'''


#2.2.1
allwords, articlewords, articletitles = nf.getarticlewords()

#print "allwords:\n", allwords, "\narticlewords:\n", articlewords, "articletitles:", articletitles

#2.2.2
result = nf.makematrix(allwords, articlewords, articletitles)
wordvec, wordInArt, articletitles = result
#print "wordVe:\n", wordVec, "\nwordInArt:\n", wordInArt, "\narticletitles:\n", articletitles


#2.2.3
awMatrix = nf.transformMatrix(wordInArt)

#2.2.4
result = nf.nnmf(awMatrix, 15, 10)
W, H = result



#2.3
result = nf.showfeatures(W,H,articletitles,wordvec)
featwords, imparticles = result
print '\n' + '#' * 50
print '6 most important words per feature:'
pp.pprint(featwords)
print '\n' + '#' * 50
print '3 most important articles per feature:'
pp.pprint(imparticles)

for index, feat in enumerate(featwords) :
    print 'Feature %d: ' %index
    print 'Most important words:'
    print ", ".join(feat)
    print 'Most important articles:'
    print " ", ",\n  ".join(imparticles[index])
    print '-' *64
    
    

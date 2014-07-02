# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np

import newsfeatures_dummy as nf


#2.1 Feeds einbinden
allfeeds = nf.scrape_feedlist(load_from_disk=True)

print 'printing loaded feeds:'
for key, value in allfeeds.items():
    print key, ": ", value

print "\n", "-" * 64, "\n"



#2.2.1 Worte sammeln
#TODO use named tuples instead of tuples
allwords, articlewords, articletitles = nf.getarticlewords()

#2.2.2 Die Artikel/Wort Matrix
result = nf.makematrix(allwords, articlewords)
wordVec, wordInArt = result

#2.2.3 Repraesentation


#convert wordInArt to matrix

#2.2.4 Implementierung der NNMF
#nf.nnmf()

#2.3
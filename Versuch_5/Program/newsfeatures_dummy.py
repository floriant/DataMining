# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np

import newsfeatures21 as nf21
import newsfeatures221 as nf221
import newsfeatured222_2 as nf222
import newsfeatures224 as nf224

#TODO
print "newsfeatures_dummy should be merged to newsfeatures"


def scrape_feedlist(load_from_disk=True):
    return nf21.scrape_feedlist(load_from_disk)


def getarticlewords():
    return nf221.getarticlewords()


def makematrix(allw, articlew):
    nf222.makematrix(allw, articlew)
    return (nf222.wordvec, nf222.wordInArt)


def nnmf(A, m, it):
    return nf224.nnmf(A, m, it)
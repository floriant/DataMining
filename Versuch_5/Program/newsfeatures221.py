# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 15:16:33 2014
"""
import re
import pprint as pp

#http://www.nltk.org/install.html
from nltk.corpus import stopwords
sw = stopwords.words( 'english' )


"""
allwords=
{ 'aided ':1,'actionfor':1, 'ambitions the ':1,'reboot':1, 'four':2, . . .
articlewords [0]=
{'accuses':1, 'into': 1,'racism':1, 'racial':2, 'debate': 1 , . . .
articletitles=
[ u 'Obama stokes racial passions,police anger' , u 'Mayors , rabbis arrested in NJ ' , . . .
"""
allwords= {}
articlewords = {}
articletitles = {}


def separatewords(text) :
    splitter=re.compile('\\W*')
    return [ s.lower() for s in splitter.split(text) if len (s)>4 and s not in sw ]

def getarticlewords():
    # init
    allwords= {}
    articlewords = {}
    articletitles = {}    
    
    #allfeeds = scrape_feedlist() 
    #local Test
    allfeeds = { 'War': 'War: tank bomb obama', 
                'Crisis': 'Crisis: Obama, bank collaps',
                'Soccer': 'Soccer: Goal, Win, Ball'}
    
    #add words to dicts
    for key, value in allfeeds.items():
        print 'Feeds: ', key, value
        for item in separatewords(value) :
            #print value
            if item in allwords :
                allwords[item] = allwords[item] + 1
            else:
                allwords[item] = 1;
                
        
if __name__ == "__main__":
    getarticlewords()
    pp.pprint(allwords)
    print "-" * 20
    pp.pprint(articlewords)
    print "-" * 20
    pp.pprint(articletitles)
    print "-" * 20
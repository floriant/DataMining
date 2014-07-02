# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 15:16:33 2014
"""
import re
import pprint as pp
import newsfeatures21 as n21

#http://www.nltk.org/install.html
# >>> import nltk
# >>> nltk.download() irgendwo im zweiten Reiter 'stopwords'
from nltk.corpus import stopwords
sw = stopwords.words( 'english' )


#Testdata
"""
allwords=
{ 'aided ':1,'actionfor':1, 'ambitions the ':1,'reboot':1, 'four':2, . . .
articlewords [0]=
{'accuses':1, 'into': 1,'racism':1, 'racial':2, 'debate': 1 , . . .
articletitles=
[ u 'Obama stokes racial passions,police anger' , u 'Mayors , rabbis arrested in NJ ' , . . .
"""

#Initialise global variables
allwords= {}
articlewords = []
articletitles = []


def separatewords(text) :
    splitter=re.compile('\\W*')
    return [ s.lower() for s in splitter.split(text) if len (s)>4 and s not in sw ]

def getarticlewords():
    # init

    global allwords
    global articlewords
    global articletitles
    allwords= {}
    articlewords = []
    articletitles = []    
    
    #load from disc:
    allfeeds = n21.scrape_feedlist()         
    #reloade from web:
    #allfeeds = n21.scrape_feedlist(False) 
    #local Test:
    #allfeeds = { 'War': 'War: tank bomb obama', 'Crisis': 'Crisis: Obama, bank collaps', 'Soccer': 'Soccer: Goal, Win, Ball'}
              
    #add titles and words
    for key, value in allfeeds.items():
        articletitles.append(key)
        words = {}
        for item in separatewords(value) :
            #add allwords            
            if item in allwords :
                allwords[item] = allwords[item] + 1
            else:
                allwords[item] = 1;
                
            #add articlewords
            if item in words :
                words[item] = words[item] + 1
            else:
                words[item] = 1;
        articlewords.append(words)
    
        
if __name__ == "__main__":
    getarticlewords()
    print "-" * 20
    pp.pprint(allwords)
    print "-" * 20
    pp.pprint(articlewords)
    print "-" * 20
    pp.pprint(articletitles)
    print "-" * 20
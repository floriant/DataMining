# -*- coding: utf-8 -*-
import re
import pprint as pp

def getwords(doc, mi=3, ma=20):
    doc = doc.lower()
    nonAlpha = re.compile('[^\wßäöüÄÖÜ]')
    doc = nonAlpha.sub( ' ', doc)    
    #print(doc)
    clean = []
    clean = doc.split()   
    #pp.pprint(clean)
    worddict = {}
    for w in clean:
        if len(w)>=mi and len(w)<=ma:
            worddict[w] = 1
    #pp.pprint(worddict)
    return worddict

class Classifier():
    def __init__(self,getfeatures):
        self.fc = {}
        self.cc = {'Good':0,'Bad':0}
        self.getfeatures = getfeatures
    def incf(self, f, cat):        
        if f not in self.fc:
            goobad = {'Good':0,'Bad':0}
            goobad[cat] = 1
            #print(goobad)
            self.fc[f] = goobad
        else:
            self.fc[f][cat] = self.fc[f][cat] + 1
        #print(self.fc)
    
    def incc(self, cat):
        self.cc[cat] = self.cc[cat] + 1
        #print(self.cc)
    def fcount(self, f, cat):
        return self.fc[f][cat]
    def catcount(self,cat):
        return self.cc[cat]
    def totalcount(self):
        #TODO iterate over all classes
        return self.cc['Good'] + self.cc['Bad']
    def train(self, item, cat):
        wlist = self.getfeatures(item)
        for w in wlist:
            self.incf(w, cat)
            self.incc(cat)

    def fprob(self,f,cat):
        return ((float) (self.fc[f][cat]) / self.cc[cat] )

    def weightedprob(self,f,cat):
        #TODO: an initprob rumspielen        
        initprob = 0.5
        count = self.fcount(f,'Good') + self.fcount(f,'Bad')
        return (initprob + count* self.fprob(f, cat)) / (1 + count)

    def prob(self, item, cat):
        product = 1
        #use weightedprob here to avoid * 0
        for f in self.getfeatures(item):
            product *= self.weightedprob(f, cat)
        return (product* self.cc[cat]) / self.totalcount()
    def decide(self, item):
        if self.prob(item, 'Good') > self.prob(item, 'Bad'):
            return 'Good'
        else:
            return 'Bad'
        
    

#print getwords("1 12 123 Hallo mehr WÖÖÖ?ÖRTtörür 1ß2ß3ß4 :hey/srjsrtz lllllllllllllllllllllllllllllllllllllllllllllllllllllllllangeswort")

classinst = Classifier(getwords)
classinst.incf('horst', 'Bad')
classinst.incf('horst', 'Bad')
classinst.incf('horst', 'Good')
classinst.incc('Good')
classinst.incc('Bad')
classinst.incc('Bad')
#print(classinst.fcount('horst', 'Bad'))
#print(classinst.catcount('Good'))
#print(classinst.totalcount())
classinst.train('RoRoRororksgki Money kagga kaggagaga tatotu 1','Good')
classinst.train('Penis Viagra Free Money Money Money Yo', 'Bad')
# Money kommt nur einmal rein (wegen dict)
classinst.train('Money Boy Penis Yo', 'Bad')
classinst.train('Penis', 'Bad')
#pp.pprint(classinst.fc)
#pp.pprint(classinst.fprob('money', 'Bad'))
#pp.pprint(classinst.weightedprob('money', 'Bad'))
pp.pprint(classinst.prob('Penis','Good'))
pp.pprint(classinst.prob('Penis','Bad'))
pp.pprint(classinst.decide('RoRoRororksgki Money kagga kaggagaga tatotu 1'))
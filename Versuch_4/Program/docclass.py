# -*- coding: utf-8 -*-
import re
import pprint as pp


def getwords(doc, mi=3, ma=20):
    doc = doc.lower() #.encode('utf-8')
 #   doc = re.sub(r'[^\x00-\x7F]+', '', doc)

    #nonAlpha = re.compile('[^\wßäöüÄÖÜ]')
    nonAlpha = re.compile('[^a-zäöüß]')
    doc = nonAlpha.sub(' ', doc)

    clean = []
    clean = doc.split()
    #pp.pprint(clean)
    worddict = {}
    for w in clean:
        if mi <= len(w) <= ma:
            worddict[w] = 1
    #pp.pprint(worddict)
    return worddict


class Classifier():
    def __init__(self, getfeatures, classes):
        self.fc = {}
        self.classes = classes
        self.cc = self.create_classes_dictionary()

        self.getfeatures = getfeatures

    def create_classes_dictionary(self):
        #create_classes_dictionary(['Good', 'Bad']) => {'Good': 0, 'Bad': 0}
        result = {}
        for cls in self.classes:
            result[cls] = 0

        return result

    def incf(self, f, cat):
        if f not in self.fc:
            self.fc[f] = self.create_classes_dictionary()
            self.fc[f][cat] = 1

        else:
            self.fc[f][cat] += 1

    def incc(self, cat):
        self.cc[cat] += 1

    def fcount(self, f, cat):
        return self.fc.get(f, {cat: 0})[cat]

    def catcount(self, cat):
        return self.cc[cat]

    def totalcount(self):
        return sum(self.cc.itervalues())

    def train(self, item, cat):
        wlist = self.getfeatures(item)
        for w in wlist:
            self.incf(w, cat)
            self.incc(cat)

    def fprob(self, f, cat):
        return ((float)(self.fc.get(f, {cat: 0})[cat]) / self.cc[cat])

    def weightedprob(self, f, cat):
        #TODO: an initprob rumspielen        
        initprob = 0.5
        count = 0
        for cls in self.classes:
            count += self.fcount(f, cls)

        return (initprob + count * self.fprob(f, cat)) / (1 + count)

    def prob(self, item, cat):
        product = 1
        """use weightedprob here to avoid * 0"""
        for f in self.getfeatures(item):
            product *= self.weightedprob(f, cat)
        return (product * self.cc[cat]) / self.totalcount()

    def decide(self, item):
        max_val = -1
        max_cls = ''

        for cls in self.classes:
            prob = self.prob(item, cls)
            if prob > max_val:
                max_val = prob
                max_cls = cls

        return max_cls



def assignment_2_2_test_spam():
    training_data = [
        ['nobody owns the water', 'Good'],
        ['the quick rabbit jumps fences', 'Good'],
        ['buy pharmaceuticals now', 'Bad'],
        ['make quick money at the online casino', 'Bad'],
        ['the quick brown fox jumps', 'Good'],
        ['next meeting is at night', 'Good'],
        ['meeting with your superstar', 'Bad'],
        ['money like water', 'Bad'],
        ['Nigeria prince scam', 'Bad'],
        ['this übel is a good one', 'Good']
    ];

    test_data = 'the money jumps übel'

    classifier = Classifier(getwords, ['Good', 'Bad'])
    for keyVal in training_data:
        classifier.train(keyVal[0], keyVal[1])

    classification = classifier.decide(test_data)
    prob_good = classifier.prob(test_data, 'Good')
    prob_bad = classifier.prob(test_data, 'Bad')

    print("'%s' was classified as '%s' (good: %f / bad: %f)" % (test_data, classification, prob_good, prob_bad))


def first_tests():
    #print getwords("1 12 123 Hallo mehr WÖÖÖ?ÖRTtörür 1ß2ß3ß4 :hey/srjsrtz lllllllllllllllllllllllllllllllllllllllllllllllllllllllllangeswort")

    classinst = Classifier(getwords, ['Good', 'Bad'])
    classinst.incf('horst', 'Bad')
    classinst.incf('horst', 'Bad')
    classinst.incf('horst', 'Good')
    classinst.incc('Good')
    classinst.incc('Bad')
    classinst.incc('Bad')
    #print(classinst.fcount('horst', 'Bad'))
    #print(classinst.catcount('Good'))
    #print(classinst.totalcount())
    classinst.train('RoRoRororksgki Money kagga kaggagaga tatotu 1', 'Good')
    classinst.train('Penis Viagra Free Money Money Money Yo', 'Bad')
    # Money kommt nur einmal rein (wegen dict)
    classinst.train('Money Cash Penis Yo', 'Bad')
    classinst.train('Penis', 'Bad')
    #pp.pprint(classinst.fc)
    #pp.pprint(classinst.fprob('money', 'Bad'))
    #pp.pprint(classinst.weightedprob('money', 'Bad'))
    pp.pprint(classinst.prob('Penis', 'Good'))
    pp.pprint(classinst.prob('Penis', 'Bad'))
    pp.pprint(classinst.decide('RoRoRororksgki Money kagga kaggagaga tatotu 1'))


if __name__ == "__main__":
    #first_tests()
    assignment_2_2_test_spam()
    pass

    print getwords('"Günther Jauch": Isis-Vormarsch – "Das Problem liegt in der Türkei" Günther Jauch diskutierte den Vormarsch islamistischer Gotteskrieger im Irak. Norbert Röttgen kritisierte das Wegschauen der Deutschen, ein Experte lenkte den Blick auf die Türkei.')


# -*- coding: utf-8 -*-
import re
import pprint as pp


def getwords(doc, mi=3, ma=20):
    #remove unwanted characters
    nonAlpha = re.compile('[^a-zäöüß]')
    doc = nonAlpha.sub(' ', doc.lower())

    #create a dictionary containing each word
    clean = doc.split()
    worddict = {}
    for w in clean:
        if mi <= len(w) <= ma:
            worddict[w] = 1

    return worddict


class Classifier():
    def __init__(self, getfeatures, classes):
        self.fc = {}
        self.classes = classes
        self.cc = self.create_classes_dictionary()
        self.initprob = 0.5

        self.getfeatures = getfeatures

    #creates a base dictionary to be used for each word with the classes
    #pro: the checks if a class exists in the dictionary are not needed
    #con: slight increase of memory usage
    def create_classes_dictionary(self):
        #create_classes_dictionary(['Good', 'Bad']) => {'Good': 0, 'Bad': 0}
        result = {}
        for cls in self.classes:
            result[cls] = 0

        return result

    #increase the passed feature's counter for the passed category
    def incf(self, f, cat):
        if f not in self.fc:
            self.fc[f] = self.create_classes_dictionary()

        self.fc[f][cat] += 1

    #increase the category counter for the passed category
    def incc(self, cat):
        self.cc[cat] += 1

    #returns the passed feature's counter for the passed category
    def fcount(self, f, cat):
        #get is used because it provides a default if the value does not exist
        return self.fc.get(f, {cat: 0})[cat]

    #returns the counter of the passed category
    def catcount(self, cat):
        return self.cc[cat]

    #returns the sum of all elements
    def totalcount(self):
        return sum(self.cc.itervalues())

    #train a new element and add it to the passed category
    def train(self, item, cat):
        wlist = self.getfeatures(item)
        for w in wlist:
            self.incf(w, cat)
            self.incc(cat)

    #return the probability for the passed feature for the passed category
    def fprob(self, f, cat):
        return ((float)(self.fc.get(f, {cat: 0})[cat]) / self.cc[cat])

    #calculate the weighted probability (avoids 0 for non-exististing words)
    def weightedprob(self, f, cat, initprob=0.5):
        if initprob != 0.5:
            self.initprob = 0.5

        count = 0
        for cls in self.classes:
            count += self.fcount(f, cls)

        return (self.initprob + count * self.fprob(f, cat)) / (1 + count)

    #return the weighteted probability for the passed feature for the passed category
    def prob(self, item, cat):
        product = 1

        for f in self.getfeatures(item):
            product *= self.weightedprob(f, cat)
        return (product * self.cc[cat]) / self.totalcount()

    #return the class the fits the passed item best
    def decide(self, item):
        max_val = -1
        max_cls = ''

        for cls in self.classes:
            prob = self.prob(item, cls)
            if prob > max_val:
                max_val = prob
                max_cls = cls

        return max_cls


#Exercise 2.2
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
        ['this is a good one', 'Good']
    ];

    test_data = 'the money jumps'

    classifier = Classifier(getwords, ['Good', 'Bad'])
    """Initprob can be used to decrease or increase the influence of not-learned words"""
    classifier.initprob = 0.5

    for keyVal in training_data:
        classifier.train(keyVal[0], keyVal[1])

    classification = classifier.decide(test_data)
    prob_good = classifier.prob(test_data, 'Good')
    prob_bad = classifier.prob(test_data, 'Bad')

    print("'%s' was classified as '%s' (good: %f / bad: %f)" % (test_data, classification, prob_good, prob_bad))


if __name__ == "__main__":
    #first_tests()
    assignment_2_2_test_spam()
    pass

    print getwords('"Günther Jauch": Isis-Vormarsch – "Das Problem liegt in der Türkei" Günther Jauch diskutierte den Vormarsch islamistischer Gotteskrieger im Irak. Norbert Röttgen kritisierte das Wegschauen der Deutschen, ein Experte lenkte den Blick auf die Türkei.')


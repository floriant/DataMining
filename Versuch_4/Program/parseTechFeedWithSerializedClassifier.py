import feedparser
import docclass as dc
import pprint as pp
import pickle as pickle

def stripHTML(h):
    p = ''
    s = 0
    for c in h:
        if c == '<':
            s = 1
        elif c == '>':
            s = 0
            p += ' '
        elif s == 0:
            p += c
    return p


test = [
    "http://rss.golem.de/rss.php?r=sw&feed=RSS0.91",
    'http://newsfeed.zeit.de/politik/index',
    'http://www.welt.de/?service=Rss'
]

countnews = {}
countnews['tech'] = 0
countnews['nontech'] = 0
countnews['test'] = 0

test_news = {'tech': [], 'nontech': []}


serialized_classifier_filename = 'classifier.serialized'
serialized_classifier = open(serialized_classifier_filename, 'rb')
classifier = pickle.load(serialized_classifier)
serialized_classifier.close()

print 'Classifier was loaded from file ' + serialized_classifier_filename


print "--------------------News from test------------------------"
for feed in test:
    f = feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext = stripHTML(e.title + ' ' + e.description)
        print fulltext
        countnews['test'] += 1
        classification = classifier.decide(fulltext)
        test_news[classification].append([fulltext,
            classifier.prob(fulltext, 'tech'),
            classifier.prob(fulltext, 'nontech')]
        )

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print 'Number of used test samples', countnews['test']
print "----------------------------------------------------------------"

print '-' * 64, "\n"

#pp.pprint(test_news)

print '-' *64, "\n", '-'*64

for cls in test_news:
    print '-'*64, '\ncategorized as %s:' % (cls)
    for entry in test_news[cls]:
        print entry[0]

print '-'*64, '\n', 'Number of used test samples', countnews['test']
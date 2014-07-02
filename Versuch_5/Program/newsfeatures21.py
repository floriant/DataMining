# -*- coding: utf-8 -*-
import pprint as pp

feedlist = ['http://feeds.reuters.com/reuters/topNews',
            'http://feeds.reuters.com/reuters/businessNews',
            'http://feeds.reuters.com/reuters/worldNews',
            'http://feeds2.feedburner.com/time/world',
            'http://feeds2.feedburner.com/time/business',
            'http://feeds2.feedburner.com/time/politics',
            'http://rss.cnn.com/rss/edition.rss',
            'http://rss.cnn.com/rss/edition_world.rss',
            'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml',
            'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/europe/rss.xml',
            'http://www.nytimes.com/services/xml/rss/nyt/World.xml'
            'http://www.nytimes.com/services/xml/rss/nyt/Economy.xml'
]


def scrape_feedlist(load_from_disk=True):

    def writeToFile(obj, filename):
        f = open(filename, 'w')
        f.write(str(obj))
        f.close()


    def readFromFile(filename):
        f = open(filename, 'r')
        result = eval(f.read())
        f.close()
        return result


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

    def download_feeds():
        import feedparser

        result = {}
        key = ""
        value = ""
        for feed in feedlist:
            f = feedparser.parse(feed)
            print "download feed %s:\n" % feed, "-" * 64

            for e in f.entries:
                key = stripHTML(e.title)
                value = key + " " + stripHTML(e.description)
                print key + ': ' + value
                result[key] = value

        print "-" * 64, "\n", "%d Entries were downloaded from the feed list" % (len(result))

        writeToFile(result, allfeeds_file)
        return result

    allfeeds_file = '../doc/allfeeds.txt'
    result = {}
    if load_from_disk:
        result = readFromFile(allfeeds_file)

    if not load_from_disk or len(result) == 0:
        result = download_feeds()

    return result


if __name__ == "__main__":
    allfeeds = scrape_feedlist(load_from_disk=True)

    #pp.pprint(allfeeds)
    for key, value in allfeeds.items():
        print value

    pass
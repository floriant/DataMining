# -*- coding: utf-8 -*-
import pprint as pp
import numpy as np


#set to false to suppress output
debug = True


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

#######
# 2.1 #
#######
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


#########
# 2.2.1 #
#########
def separatewords(text):
    import re
    from nltk.corpus import stopwords

    sw = stopwords.words( 'english' )
    splitter = re.compile('\\W*')
    return [ s.lower() for s in splitter.split(text) if len (s)>4 and s not in sw ]


def getarticlewords():
    allwords = {}
    articlewords = []
    articletitles = []

    #set load_from_disk to False to reload feeds from web
    allfeeds = scrape_feedlist(load_from_disk=True)

    #add titles and words
    for key, value in allfeeds.items():
        articletitles.append(key)
        words = {}
        for item in separatewords(value):
            #add allwords
            if item in allwords:
                allwords[item] += 1
            else:
                allwords[item] = 1

            #add articlewords
            if item in words :
                words[item] += 1
            else:
                words[item] = 1
        articlewords.append(words)

    return (allwords, articlewords, articletitles)


#########
# 2.2.2 #
#########


# makematrix Function to write the wordvec and wordInArt Global Variables
#
# Params
# allw: Dict - Dictionary that contains all Words with their overall count.
# articlewords: Dict - Dictionary that contains numeric Keys for each Article which contains Words as Keys and WordCount as Value
#
# Note:
# The wordvec and wordInArt results, will be written as Dict.
# This way no Information about the Words gets lost.
def makematrix(allw, articlew):
    temp_articlew = {}
    for index, value in enumerate(articlew):
        temp_articlew[index] = value

    articlew = temp_articlew

    # Declaring Global Vars
    wordvec = {}
    wordInArt = {}

    # Removing words that have a overall Wordcount >= 4
    trimmedV = {}
    for word in allw:
        if allw[word] >= 4:
            trimmedV[word] = allw[word]

    # Removing words that appear > 60% in all Articles
    #
    # artP: Percent per Article occurence
    # percentage: Percentage counting Value
    # trimmedPercent: Copy of trimmedV since Python doesnt allow changing Dicts in a Loop
    artP = (100 / len(articlew))
    percentage = 0
    trimmedPercent = trimmedV.copy()
    for wordV in trimmedV:
        for article in articlew:
            if articlew[article].has_key(wordV):
                percentage += artP
        if percentage < 60:
            trimmedPercent.pop(wordV)
        percentage = 0

    # Debugging output for the two Word Reduction Steps
    print('###########################################')
    print('############## >= 4 Check #################')
    print('###########################################')
    print(trimmedV)
    print('###########################################')
    print('############## > 60% Check ################')
    print('###########################################')
    print(trimmedPercent)

    # Create Article/Word Matrix
    #
    # We Loop trough the articlewords for vector i
    # We Loop trough trimmedPercent for vector j
    awMatrix = {}
    valueCount = 0
    for article in articlew:
        awMatrix[article] = {}
        valueCount = 0
        for wordAW in trimmedPercent:
            wordTrashhold = wordAW
            if wordAW in articlew[article]:
                awMatrix[article][wordAW] = articlew[article][wordAW]
                valueCount += 1
            else:
                awMatrix[article][wordAW] = 0

        # Checking if the Article has only 0 values
        # then pop the Artice out of the Dict
        if valueCount == 0:
            awMatrix.pop(article)

    # Printing the awMatrix for Debugging Purposes
    print('###########################################')
    print('######## The Article/Word Matrix ##########')
    print('###########################################')
    pp.pprint(awMatrix)

    # Writing the wordvec and wordInArt Variables
    # Note: This should give us an reference, so no Additional Space is wasted in RAM
    wordvec = trimmedPercent
    wordInArt = awMatrix

    # Creating Text File with Matrix
    file = open('../res/awMatrix.txt', 'w')
    wordvecText = ''
    # First Line consists of wordvec
    for i, txtWord in enumerate(trimmedPercent):
        if i != len(trimmedPercent)-1:
            wordvecText += txtWord + ','
        else:
            wordvecText += txtWord + '\n'
    print('###########################################')
    print('###### Text to Write from wordvec #########')
    print('###########################################')
    print wordvecText

    # Creating the Data from wordInArt Matrix
    wordInArtText = ''
    for txtArticle in awMatrix:
        for i, txtData in enumerate(awMatrix[txtArticle]):
            if i != len(awMatrix[txtArticle])-1:
                wordInArtText += str(awMatrix[txtArticle][txtData]) + ','
            else:
                wordInArtText += str(awMatrix[txtArticle][txtData]) + '\n'
    print('###########################################')
    print('###### Text to Write from wordInArt #######')
    print('###########################################')
    print wordInArtText

    # Writing to File
    file.write(wordvecText)
    file.write(wordInArtText)
    file.close()

    return (wordvec, wordInArt)


#########
# 2.2.3 #
#########


# transformMatrix function to Transform the wordInArt Dict to a Numpy Matrix
#
# Params:
# awDict - Representation of the wordInArt Dict
#
# Returns the Article/Word Matrix as numpy.matrix Object
def transformMatrix(awDict):
    matrixList = []
    # Iterating rough awDict and Converting Data into a nested List
    for row in awDict:
        rowList = []
        print(row)
        for i, col in enumerate(awDict[row]):
            rowList.append(awDict[row][col])
        matrixList.append(rowList)
    # Transforming nested List to an numpy Matrix
    awNumpyMatrix = np.matrix(matrixList)

    if debug:
        print('###########################################')
        print('###### The Article/Word as np.matrix ######')
        print('###########################################')
        print(awNumpyMatrix)

    return awNumpyMatrix



#########
# 2.2.4 #
#########

#A and B are of type numpy.matrix
#returns the summed euclidean distance of the passed matrices
def cost(A, B):
    k = 0
    #create iterators
    iteratorA = A.flat
    iteratorB = B.flat

    try:
        while True:
            #iterate over all elements in both matrices
            Aij = iteratorA.next()
            Bij = iteratorB.next()
            k += pow(Aij - Bij, 2)
            #print "Aij=%d | Bij=%d" % (Aij, Bij)

    except StopIteration:
        pass  #needed because the iterator does not know if there are more elements coming

    return k


# Calculate NNMF
# parameters:
#     A: non-negative Matrix
#     m: count of merkmal
#     it: number of iterations
# returns: {
#     H: Merkmalsmatrix
#     W: Gewichtsmatrix
# }
def nnmf(A, m, it):
    #get row count and column count of A
    r, c = A.shape

    #step 2:
    ## assert that m < c, else: throw exception
    if m >= c:
        #throw Argument Error
        print "nnmf throws argument Error: m must be smaller than c (count of columns)"
        return

    #step 3+4:
    #initialize matrices H and W
    H = np.matrix(np.random.randint(1, 7, (m, c))) #0 needs to be excluded
    W = np.matrix(np.random.randint(1, 7, (r, m))) #0 needs to be excluded

    if debug:
        print "shape of H: ", H.shape, "\nshape of W: ", W.shape
        pp.pprint({'H': H, 'W': W})

    #step 5:
    while it > 0:
        #calculate current product of H and W
        #a)
        B = W * H
        k = cost(A, B)

        if not debug:
            pp.pprint({'A': A, 'B': B})
            print "cost: %d" % k

        #break if desired matrix and factorized matrix are very similar
        if k < 5:
            break

        #b) recalculate H
        # Hij = Hij * (W_transposed * A)ij / (W_transposed * W * H)ij
        temp1 = np.array(W.T * A)
        temp2 = np.array(W.T * W * H)
        H = np.matrix( np.array(H) * np.true_divide(temp1, temp2) ) #normal divide floors the results

        if not debug:
            print "shape of H: ", H.shape, "H:"
            pp.pprint(H)

        #c) recalculate W
        #Wij = Wij * (A * H_transposed)ij / (W * H * H_transposed)ij
        nextW = np.array(W) * np.true_divide(np.array(A * H.T), np.array(W * H * H.T)) #normal divide floors the results
        W = np.matrix( nextW )


        it -= 1
        if not debug:
            print "current values: (%d more iterations)\n" % it
            print "W:\n", W, "\nH:\n", H
            print "-"*64

    #return {'H': H, 'W': W}
    return W, H
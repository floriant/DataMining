import pprint as pp

# Example Data for Testing
allwords = {'aided':3, 'actionfor': 2, 'ambitionsthe':2, 'reboot':4, 'four':8, 'accused': 10, 'into': 3, 'racism': 4, 'debate':3}
articlewords = {}
articlewords[0] = {'accused': 1, 'into': 1, 'racism': 2, 'debate': 1}
articlewords[1] = {'accused': 1, 'aided': 1, 'actionfor': 2, 'ambitionsthe': 1, 'reboot': 1, 'four': 2}
articlewords[2] = {'aided':1, 'ambitionsthe':1, 'reboot':1, 'four':2, 'into': 1, 'debate':1}
articlewords[3] = { 'reboot':1, 'four':2, 'accused': 2}
articlewords[4] = {'aided':1, 'actionfor': 1, 'ambitionsthe':1, 'reboot':1, 'four':2, 'accused': 2, 'into': 1, 'racism': 2, 'debate':1}

# Global Variables used for article Word Matrix
wordvec = {}
wordInArt = {}

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

    # Removing words that have a overall Wordcount >= 4
    trimmedV = {}
    for word in allwords:
        if allwords[word] >= 4:
            trimmedV[word] = allwords[word]

    # Removing words that appear > 60% in all Articles
    #
    # artP: Percent per Article occurence
    # percentage: Percentage counting Value
    # trimmedPercent: Copy of trimmedV since Python doesnt allow changing Dicts in a Loop
    artP = (100 / len(articlewords))
    percentage = 0
    trimmedPercent = trimmedV.copy()
    for wordV in trimmedV:
        for article in articlewords:
            if articlewords[article].has_key(wordV):
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
    for article in articlewords:
        awMatrix[article] = {}
        for wordAW in trimmedPercent:
            if wordAW in articlewords[article]:
                awMatrix[article][wordAW] = articlewords[article][wordAW]
            else:
                awMatrix[article][wordAW] = 0

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


makematrix(allwords, articlewords)
print("end")
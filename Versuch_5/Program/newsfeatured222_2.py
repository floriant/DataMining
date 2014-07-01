import pprint as pp
allwords = {'aided':3, 'actionfor': 2, 'ambitionsthe':2, 'reboot':4, 'four':8, 'accused': 10, 'into': 3, 'racism': 4, 'debate':3}
articlewords = {}
articlewords[0] = {'accused': 1, 'into': 1, 'racism': 2, 'debate': 1}
articlewords[1] = {'accused': 1, 'aided': 1, 'actionfor': 2, 'ambitionsthe': 1, 'reboot': 1, 'four': 2}
articlewords[2] = {'aided':1, 'ambitionsthe':1, 'reboot':1, 'four':2, 'into': 1, 'debate':1}
articlewords[3] = { 'reboot':1, 'four':2, 'accused': 2}
articlewords[4] = {'aided':1, 'actionfor': 1, 'ambitionsthe':1, 'reboot':1, 'four':2, 'accused': 2, 'into': 1, 'racism': 2, 'debate':1}
print allwords

wordvec = {}
wordInArt = {}


def makematrix(allw, articlew):
    # Removing Words with less tan 4 occourences
    trimmedV = {}
    for word in allwords:
        print(allwords[word])
        if allwords[word] >= 4:
            trimmedV[word] = allwords[word]
    print(trimmedV)

    # Removing Words with less than 60% occurence
    artP = (100 / len(articlewords))
    percentage = 0
    trimmedPercent = trimmedV.copy()
    print(artP)
    print("--------------AllWords V")
    print(trimmedV)
    print("--------------//")
    for wordV in trimmedV:
        print("--------------Current Word V")
        print(wordV)
        print("--------------//")
        for article in articlewords:
            print("--------------Current Article")
            print(article)
            print(articlewords[article])
            print("--------------//")
            #for aword in articlewords[article]:
            #    print(aword)
            print("--------------Trimmed V word V and haskey?")
            print(wordV)
            print(articlewords[article].has_key(wordV))
            print("--------------//")
            if articlewords[article].has_key(wordV):
                percentage += artP
            print("#####################################################")
        if percentage < 60:
            print percentage
            trimmedPercent.pop(wordV)
        percentage = 0
    print(trimmedV)
    print(trimmedPercent)

    #Wir verwenden anstelle listen Dictionarys
    #Wenn man Listen uebergibt verliert man die reihenfolge der worte
    #durch dictionarys kann man jederzeit eine semantische zuordnung vornehmen.

    print('######################################################')
    print('######################################################')
    print('######################################################')
    print('######################################################')

    # Create Article/Word Matrix
    awMatrix = {}
    for article in articlewords:
        print(article)
        awMatrix[article] = {}
        for wordAW in trimmedPercent:
            #print(wordAW)
            #print(allwords[wordAW])
            awMatrix[article][wordAW] = allwords[wordAW]
    pp.pprint(awMatrix)

    wordvec = trimmedPercent
    wordInArt = awMatrix

makematrix(allwords, articlewords)
print("end")
from os.path import isdir,join,normpath
from os import listdir

from PIL import Image

import pprint as pp
import heapq as hq

from numpy import asfarray,dot,argmin,zeros
from numpy import average,sort,trace,argsort
from numpy.linalg import svd,eigh
from numpy import concatenate, reshape
from math import sqrt
import scipy.spatial.distance as ssd

import tkFileDialog

def parseDirectory(directoryName,extension):
    '''This method returns a list of all filenames in the Directory directoryName. 
    For each file the complete absolute path is given in a normalized manner (with 
    double backslashes). Moreover only files with the specified extension are returned in 
    the list.
    '''
    if not isdir(directoryName): return
    imagefilenameslist=sorted([
        normpath(join(directoryName, fname))
        for fname in listdir(directoryName)
        if fname.lower().endswith('.'+extension)            
        ])
    return imagefilenameslist

#####################################################################################
# Implement required functions here
#
#
#
def generateListOfImages(ListOfTrainFiles) :
    imgfiles = []
    for filename in ListOfTrainFiles :   
        im = Image.open(filename)
        imgfiles.append(im)
    return imgfiles

def imgToVec(img) :
    vec = asfarray(img)
    #norm
    vec = vec / vec.max()
    vec = vec.flatten()
    return vec

def convertImgListToNumpyData(imgList) :
    
    imgArray = []
    for img in imgList :
        imgArray.append(imgToVec(img)) 
    return asfarray(imgArray)

def calculateEigenfaces(adjfaces,width,height,K=6) :
    CV = dot(adjfaces, adjfaces.T)
    #print CV.shape
    eigVal, eigVec = eigh(CV)
    #eigVal[5] = 999999.9
    #print eigVal
    #print argsort(eigVal)[-7:]    
    #print argsort(eigVal)[-7:][::-1]
    indices = argsort(eigVal)[-K:][::-1]  
    usub = []
    for ind in indices :
        usub.append(dot(eigVec[ind], adjfaces ))
    #print len(usub)
    
    return usub    
    
    #pp.pprint(hq.nlargest(7, eigVal))
    #for val in hq.nlargest(7, eigVal) :
    #    print eigVal.index(val)
    #largest = hq.nlargest(7, eigVal)
    #for i, j in enumerate(eigVal) :
    #    if j in largest :
    #        print i
    #        print eigVec[i]
        
    
    
        
####################################################################################
#Start of main programm

#Choose Directory which contains all training images 
#TrainDir=tkFileDialog.askdirectory(title="Choose Directory of training images")
TrainDir="../res/FaceRecogBilder/training"
#Choose the file extension of the image files
Extension='png' 
#Choose the image which shall be recognized
#testImageDirAndFilename=tkFileDialog.askopenfilename(title="Choose Image to detect")
testImageDirAndFilename="../res/FaceRecogBilder/test/1-2.png"
####################################################################################
# Implement required functionality of the main programm here
if __name__ == "__main__" :
    
    A321 = False
    A322 = True
    K = 6
    
    listOfTrainFiles = parseDirectory(TrainDir, Extension)
    
    imgList = generateListOfImages(listOfTrainFiles)
    
#######
#3.2.1#
#######
    if A321 :
        for img in imgList :
            print img.format, img.size, img.mode
    width, height = imgList[0].size
#######
#3.2.2#
#######
    ArrayOfFaces = convertImgListToNumpyData(imgList)
#######
#3.2.3#
#######
    NormedArrayOfFaces = ArrayOfFaces - average(ArrayOfFaces)
#######
#3.2.4#
#######
    eigenfaces = calculateEigenfaces(NormedArrayOfFaces,width,height,K=K)
#######
#3.2.5#
#######
    trainedFaces = []
    for face in NormedArrayOfFaces :
        trainedFaces.append(dot(face, asfarray(eigenfaces).T))
    print trainedFaces
#####
#3.3#
#####
    testImage = Image.open("../res/FaceRecogBilder/test/1-1.png")
    testImageArray = imgToVec(testImage)
    print testImageArray
    NormedTestFace = testImageArray - average(ArrayOfFaces)
    print NormedTestFace
    recTest = dot(NormedTestFace,asfarray(eigenfaces).T)
    print recTest
    mindist = 9999
    pos = -1
    for i,trainface in enumerate(trainedFaces):
        dist = ssd.euclidean(recTest, trainface)
        print i
        print dist
        if dist < mindist:
            mindist = dist
            pos = i
    print "-------------------------"
    print mindist
    print pos

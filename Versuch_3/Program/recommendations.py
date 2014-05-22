# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

import matplotlib.pyplot as plt

from math import sqrt
import numpy as np
import scipy.spatial.distance as sci


def sim_euclid(prefs,person1,person2,normed=False):
  ''' Returns a euclidean-distance-based similarity score for 
  person1 and person2. In the distance calculation the sum is computed 
  only over those items, which are nonzero for both instances, i.e. only
  films which are ranked by both persons are regarded.
  If the parameter normed is True, then the euclidean distance is divided by
  the number of non-zero elements integrated in the distance calculation. Thus
  the effect of larger distances in the case of an increasing number of commonly ranked
  items is avoided.
  '''
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1
  # len(si) counts the number of common ratings
  # if they have no ratings in common, return 0
  if len(si)==0: return 0

  # Add up the squares of all the differences
  sum_of_squares=sqrt(sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                     for item in prefs[person1] if item in prefs[person2]]))
  if normed:
     sum_of_squares= 1.0/len(si)*sum_of_squares
  return 1/(1+sum_of_squares)


def sim_pearson(prefs,p1,p2):
  '''
  Returns the Pearson correlation coefficient for p1 and p2
  '''
    
  # Get the list of commonly rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Calculate means of person 1 and 2
  mp1=np.mean([prefs[p1][it] for it in si])
  mp2=np.mean([prefs[p2][it] for it in si])
  
  # Calculate standard deviation of person 1 and 2
  sp1=np.std([prefs[p1][it] for it in si])
  sp2=np.std([prefs[p2][it] for it in si])
  
  # If all elements in one sample are identical, the standard deviation is 0. 
  # In this case there is no linear correlation between the samples
  if sp1==0 or sp2==0:
      return 0
  r=1/(n*sp1*sp2)*sum([(prefs[p1][it]-mp1)*(prefs[p2][it]-mp2) for it in si])
  return r


def sim_RusselRao(prefs,person1,person2,normed=True):
  ''' Returns RusselRao similaritiy between 2 users. The RusselRao similarity just counts the number
  of common non-zero components of the two vectors and divides this number by N, where N is the length
  of the vectors. If normed=False, the division by N is omitted.
  '''
  # Get the list of shared_items
  si={}
  commons=0
  for item in prefs[person1]: 
    if prefs[person1][item]==1 and prefs[person2][item]==1:   
        commons+=1
  #print commons
  if not normed:
      return commons
  else:
      return commons*1.0/len(prefs[person1])  
      
  


#!/usr/bin/env python
# coding: utf-8

# # Vectorisation of Text Data

# The process of converting or transforming a data set into a set of Vectors is called Vectorization.

# In[1]:


# import libraries
import pandas as pd
import sklearn as sk
import math 


# In[2]:


# Calculate dot product of two vectors, divide it by the magnitudes to find the cos(angle between them)
# Use the result as a correlation coefficient 
from collections import Counter

def cosine(vector1, vector2):
     # calculate nominator as a dot product
     intersect = set(vector1.keys()) & set(vector2.keys())
     numerator = sum([vector1[x] * vector2[x] for x in intersect])
    
     # calculate the denominator 
     sum1 = sum([vector1[x] ** 2 for x in list(vector1.keys())])
     sum2 = sum([vector2[x] ** 2 for x in list(vector2.keys())])
    
     denominator = math.sqrt(sum1) * math.sqrt(sum2)
     if not denominator:
         return 0.0
     else:
         return float(numerator)/denominator


# # Assignment

# In[3]:


with open('textfiles/A.txt', 'r', encoding='utf8', errors='ignore') as a:
    A = a.read().replace('\n', '')
with open('textfiles/B.txt', 'r', encoding='utf8', errors='ignore') as b:
    B = b.read().replace('\n', '')
with open('textfiles/C.txt', 'r', encoding='utf8', errors='ignore') as c:
    C = c.read().replace('\n', '')
    
A1 = A.split(" ") 
B1 = B.split(" ") 
C1 = C.split(" ") 

# join the sets of words to remove duplications
all= set(A1).union(set(B1).union(C1))
#print(all)


# In[4]:


def convertTextToVector(text):
    x = dict.fromkeys(all, 0) 
    for word in text:
        x[word]+=1
    return x


# In[5]:


def compareVectors():
    AVector = convertTextToVector(A1)
    BVector = convertTextToVector(B1)
    CVector = convertTextToVector(C1)
    
    corrAB = cosine(AVector, BVector)
    print("Similarity on A and B: ", corrAB)
    
    corrAC = cosine(AVector, CVector)
    print("Similarity on A and C: ", corrAC)
    
    corrBC = cosine(BVector, CVector)
    print("Similarity on B and C: ", corrBC)
    
    suggestion = ""
    
    highest = 0
    corrarray = [corrAB, corrAC, corrBC]
    for i in corrarray:
        if highest < i:
            highest = i
            
    if highest == corrAB:
        suggestion = "Text A = X, Text B = X, Text C = Y"
    elif highest == corrAC:
        suggestion = "Text A = X, Text B = Y, Text C = X"
    else:
        suggestion = "Text A = Y, Text B = X, Text C = X"
    return suggestion


# In[6]:


suggestion = compareVectors()
print(suggestion)


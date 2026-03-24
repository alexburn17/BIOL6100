# Intro to python
# March 17, 2026
# P. Alexander Burnham


# Installing libraries:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#################################
# Objects, Methods and Functions:
#################################


print("I love Python")

greeting = "Hello"

print(greeting)

scaler = 6 # ineger value

out = scaler * 3 # doing math with an obj

myList = [34, 7, 98] # create a list

myList.append(33) # so appending data in a list

len(myList) # length function

# data structres:
#--------------------------------------

# make a list of colors
a_list = ["blue", "green", "red"]

# indexing into a list:
first_el = a_list[0]
print(first_el)

# looking at data types
nums = [1,2,5,8]
chars = ["a", "b", "c"]
boolean = [True, True, False]

# mixed lists
mixed = [1,2,True, "blue", 5]

# checking data types
type(nums[0]) # type returns highest level object type

# neg indexing
mixed[-1] # returns the last element
mixed[-3] # third element from the right

# ranged indexing
mixed[1:4] # end of range not inlcusive
mixed[:4] # starts from the beginning
mixed[2:] # starting point to the end

# is an item in the list
1 in mixed

# changing elements
mixed[4] = "green"

# inserts in a specific postion without overwrite
mixed.insert(0, "start")


# list methods
mixed.pop() # removes last element and returns it
mixed.append("green") # adds to the last place
mixed.remove("start") # removes element and returns nothing

mixed.remove("start")

last = mixed.pop()

last
mixed

# list comprehension

print(mixed)

[x for x in mixed]

[x for x in mixed if isinstance(x,str)]

###############################
# dictionaries:
###############################

# manually coding a dictionary
md = {
    "first":"John",
    "last":"Smith",
    "year": 2017,
    "status":"active"
}

# creating a dicitonary with the constructor function
md2 = dict(first = "john", last = "Smith")

type(md) # what type is this
len(md) # how long is the dictionary

# data types within a dictionary
dataTypes = {
    "string":"thing",
    "integer":3,
    "float":3.14342, 
    "list":[1,2,3,"a"],
    "boolean":False
}

# calling values by using key name in brackets
dataTypes["list"]

# built in method works too
dataTypes.get("boolean")

# return all keys and values using methods in dictionary
dataTypes.keys()
dataTypes.values()

# return as a list of tuples
dataTypes.items()

# add element
dataTypes["age"] = 36

# change value within a dicitonary
dataTypes["age"] = 35
dataTypes

##############################################
# NUMPY

# creating a numpy array
arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
arr1[3]
arr1[-1]
arr1[:3]
arr1[1:5]
arr1[1:8:4] # last place in indexexing encodes every nth place in arr.boolean

# 2d array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2[2,2]
arr2[:,2]
arr2[2,:]
arr2[0:2, 0:2]

# 3d array
arr3 = np.array([[[1,2],[3,4],[5,6],[7,8]]])
arr3


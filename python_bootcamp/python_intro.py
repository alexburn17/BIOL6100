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
arr3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr3

# 3d indexing
arr3[1,0,1]

# dimensions
arr1.ndim
arr2.ndim
arr3.ndim
# shape of an array
arr1.shape
arr2.shape
arr3.shape

arr2.dtype
arr2.astype(str) 

# reshaping an array
arr1.shape
arr1.reshape(2,5)

#3d array to 2d
arr3.shape
arr3.reshape(4,2)

# combining arrays
first = np.array([1,2,3])
second = np.array([4,5,6,7,8,9])

longArray = np.concatenate((first, second))
longArray

# select axis for higher dims
newStack = np.concatenate((arr2, arr2), axis = 1)
newStack.shape

# stacking arrays
newStack = np.stack((arr2, arr2))
newStack.shape

# splitting arrays
np.array_split(arr1, 2, axis = 0)


from numpy import random

random.seed(seed = 100)
random.randint(50) # 1 value from 0 to 50 
random.rand(50) # 50 vals 0 to 1
random.rand(50, 5, 10)
random.choice(arr1) # random number from arr1
random.choice(arr1, size = (3,3))
random.choice([0,1], p = [.1, .9], size = 1000)

x = random.normal(loc = 5, scale = 3, size = 200)

plt.hist(x)
plt.show()

x = random.binomial(n = 10, p = 0.5, size = 300)
print(x)

plt.hist(x)
plt.show()

x = random.uniform(low = 1, high = 10, size = 50)
print(x)

# math 
# math between arrays
#y - x # subtraction
#y + x # addition
#y / x # division
#y * x # multiplication

x * 100

arr2 * arr2

np.mean(arr2)
np.max(arr2)

####################################################
# logic structures
####################################################

# if stat.

a = 6

if a >= 5:
    print("a is greater than or equal to 5")

# with else statement 
if a >= 5:
    print("a is greater than or equal to 5")
else:
    print("a is less than 5")

a = 3
b = 3
operation = "add"

if operation == "mult":
    y = a * b
elif operation == "div":
    y = a/b
elif operation == "add":
    y = a + b
elif operation == "sub":
    y = a - b
else:
    y = "I don't know that operation!"


#####################################
# LOOPS
#####################################

l = [10, 20]

for i in range(2):
    print(l[i])

# loop on an obj. directly 
x = ["blue", "green", "red"]

for i in x:
    print(i)

# a more complicated loop
rnd = random.uniform(low = 1, high = 5, size = 10)

outList = [] # truely empty list

rnd
arr1

for i in range(len(arr1)):
    outList.append(rnd[i] + arr1[i])

outList

# nested loop with ifelse

rnd2D = random.uniform(low = 0, high = 1, size = (3,4))

matOut = np.empty(shape = (3,4)) # why does empty repopulate with old random vals
shp = rnd2D.shape
shp

# nested loop
for i in range(shp[1]):
    for j in range(shp[0]):

        if rnd2D[i,j] >= 0.5:
            matOut[i,j] = rnd2D[i,j] * 1000
        else:
            matOut[i,j] = rnd2D[i,j] / 1000

matOut

##################################################
# PANDAS DFs
##################################################

dates = pd.date_range("20130101", periods = 6)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = list("ABCD"))

# df methods
df.head(4)
df.tail(4)

df.index # pulls the row index names
df.columns # col names

df.describe()

df.to_numpy() # numpy conversion

# indexing into pandas
df["A"]
df.loc[:, ["A", "B"]]
df["20130102":"20130104"]

# read in csv file
ds = pd.read_csv("iris.data.csv")

ds["sepal_length"] # pulling col out

ds["sepal_area"] = ds.sepal_length * ds.sepal_width

ds.head()

# fully numeric filter
df[df>.5]


# ------ DF GROUPING AND SUMMARY ------ #  
# 
# Grouping means for two vars         
mean_table = ds.groupby("species")[["petal_length","sepal_length"]].mean()

# long form dataset
ds_long = pd.melt(ds, id_vars = ['species'], 
value_vars = ["sepal_width", "sepal_length", "petal_width", "petal_length"], 
var_name = "vars", value_name = 'vals')

# group_by on long form
mult_indx = ds_long.groupby(["species", "vars"]).mean()
mult_indx

# pandas pivot
pd.pivot_table(ds_long, values = "vals", index = ["vars"], columns = ["species"], aggfunc = np.mean)
pd.pivot_table(ds_long, values = "vals", index = ["vars"], columns = ["species"], aggfunc = np.median)

# Functions

# basic function structure

###############################################
# START FUNCTION
def number_adder(a, b):
    # PURPOSE: add two nums and return the sum
    # params: a = numeric, b = numeric
    # output: numeric sum of a and b
    out = a + b
    return(out)
###############################################
# END OF FUNCTION

# running number adder
number_adder(a = 3, b = 6)

# a more complex function


###############################################
# START FUNCTION
def number_adder_two(a = None, b = None):
    # PURPOSE: add two nums and return the sum
    # params: a = numeric, b = numeric
    # output: numeric sum of a and b
    if a == None or b == None:
        out = "Please provide inputs for a and b of type numeric."
    else:
        out = a + b
    return(out)
###############################################
# END OF FUNCTION

number_adder_two(a = "out", b = 4)

# GRAPHICS - seaborn

# import seaborn
import seaborn as sns


# styles: "darkgrid" "whitegrid" "dark" "white" "ticks"
sns.s

# scatter plot

# species as column 
f = sns.relplot(
    data = ds,
    x = "sepal_width", y = "petal_length",
    style = "species", hue="species"
)

f.set_axis_labels("Sepal Width", "Petal Length", labelpad = 10)
f.legend.set_title("Species")

# 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'

f = sns.lmplot(
    data = ds,
    x = "sepal_width", y = "petal_length",
    hue="species", palette = "bright")

# four panel historgram
f = sns.displot(
    ds_long,
    x = "vals", hue="species",
    col="vars", col_wrap = 2, height = 3,
    kde = True,
)

# bar plot

sns.catplot(data=ds_long, kind = "bar", x = "species",
y = "vals", hue = "vars")

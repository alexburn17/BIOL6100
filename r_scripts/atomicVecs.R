# This is a document describing vectors in R
# 22 January 2026
# P. Alexander Burnham

#---------------------------------------------
# START OF SCRIPT

x <- 5
print(x)

plant_height <- 3 # snake case
plantHeight <- 4 #camel case
plant.height <- 2 #that's not prefered 

. # reserve for temp variable


# 1d atomic vec:
z <- c(3.2, 5, 5, 6)
print(z)
typeof(z)

z <- c(c(3.2,3),c(3,5))
z
is.character(z)

# character strings
t <- "perch"
print(t)

t <- c("perch", "bass", "trout")
print(t)
t[3]

typeof(t)
is.numeric(t)


# Logical/Boolean
z <- c(TRUE, FALSE, TRUE)
print(z)

typeof(z)

c(T, F)

# vector properties 
z <- c(1.1, 1.2, 3, 4.4)





typeof(z) # gives type
is.numeric(z) # is. gives logical

t <- as.character(z) # as. coerces variable


print(t)
typeof(t)

t <- c(1,2,"3", 4)


length(t)



# random number generator
z <- runif(5)
names(z)
print(z)

# added names
names(z) <- c("A", "B", "C", "D", "E")

names(z) <- NULL
names(z)

# special data types
z <- c(3.2, 3, 3, NA)
print(z)
typeof(z)
length(z)
typeof(z[4])

sum(z, na.rm=T)

z <- 0/0
z

z <- 1/0

# vectorization 
z <- c(10, 20, 30, 40)

y <- c(1,2,3)

z + y

# recycling
x <- c(1,2)
z + x

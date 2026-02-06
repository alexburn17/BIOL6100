# Lists, Matrices, and Data Frames
# P. Alexander Burnham
# 29 Jan. 2026

##################################################################

# creating a mat from a vector

my_vec <- 1:12

# numbers by rows
m <- matrix(data = my_vec, nrow = 4)
m

# by filling the matrix the other way
m <- matrix(data = my_vec, ncol = 3, byrow = T)
m

# lists:
my_list <- list(1:10, matrix(1:8, nrow = 4, byrow = T), letters[1:3], pi)
print(my_list)

# indexing a list
x <- my_list[[1]] # double brackets for object within list element
str(x)

# indexing into a matrix
my_list[[2]][1,2] # [rows,cols]

# naming lists

my_list2 <- list(tester=FALSE, little_m = matrix(1:9, nrow = 3))
my_list2

# named objects in lists:
my_list2$little_m[2,3]

# looking at empty place indexing
my_list2$little_m[,1]
my_list2$little_m[4] # no comma, its a vec

# unlist
unrolled <- unlist(my_list2)
unrolled[1]

# unpacking complex lists
library(ggplot2)

# create some random vars
y_var <- runif(10)
x_var <- runif(10)

# regress
my_model <- lm(y_var~x_var)

# plot it
qplot(x=x_var, y=y_var) 

# explore structure
str(summary(my_model))

# extracting p vals
summary(my_model)$coefficients["x_var","Pr(>|t|)"]

u <- unlist(summary(my_model))
print(u)

pval <- u$coefficients8
pval

# data frames

var_a <- 1:12
var_b <- rep(c("A", "B", "C"), 4)
var_c <- runif(12)

# creating a data frame from vecs
df <- data.frame(var_a, var_b, var_c)

str(df)

df$var_a[1]

# expanding the data frame
new_data <- list(var_a = 13, var_b = "D", var_c = 0.77)

# appending data
df2 <- rbind(df, new_data)

View(df2) # looking at data frames in the viewer

# add a new column to a df
df2

# using cbind
new_var <- rnorm(13)
df3 <- cbind(df2, new_var)

# using assignment operator
char_var <- rep("T", 13)
df3$charV <- char_var

# writing data frames
write.csv(df3, "data/my_dataframe.csv")

data <- read.csv("data/my_dataframe.csv")

data$var_a

# Distinctions between DFs and Mat Dims

z_mat <- matrix(data = 1:30, ncol = 3, byrow = T)

z_dframe <- as.data.frame(z_mat) # turn into DF

str(z_mat)
str(z_dframe)

head(z_mat)

z_dframe$V2[2] # correct for a DF

# column ref
z_dframe[,3]
z_mat[,3]

# one dimension referencing 
z_mat[2]
z_dframe[2]

# missing data in DFs and Mats
zd <- runif(10)
zd[c(5,7)] <- NA
print(zd)

# complete cases
complete.cases(zd)

# filter for only True
zd[complete.cases(zd)]

# which positions are missing?
which(!complete.cases(zd))

# missing data in a matrix
m <- matrix(1:20, nrow = 5)

# add missing data
m[1,1] <- NA
m[5,4] <- NA

m[complete.cases(m),]

# now get complete cases for only certain columns!
m[complete.cases(m[,c1,2)]),]







my_data <- read.table(file="data/ExcelDataTemplate.csv", header=TRUE, sep=",", comment.char="#")














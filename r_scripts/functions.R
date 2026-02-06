# A demo of user defined functions in R
# P. Alexander Burnham
# 2/5/26


################################################

# looking at existing functions

sum(3,2)
3+2

`+`(3,2)

y <- 3
`<-`(yy, 5)

print(read.table)


# Creating a function

# Start function called function name:
###################################################################
adder_subtractor <- function(x = 1, y = 2, z = TRUE){
# Name: adder_subtractor
# Operation: It does some random math depending on the value of z
# Inputs: (3 inputs): 
  # x (numeric scaler value, default = 1): one of the numbers to be operated on
  # y (numeric scaler value, default = 2): one of the numbers to be operated on
  # z (logical, default = T): A switch to decide on subracting or adding
# Outputs: numeric value resulting from addition or subtraction
  if(z == TRUE){
    out <- x + y
  }else{
    out <- x - y
  }
  
  return(out)

}
##################################################################
# End of Function


adder_subtractor(x = 7, y = 4, operation = "division")


# Hardy Weinberg Function

##########################################
# START FUNCTION:
hardy_weinberg <- function(p = runif(1)){
##########################################
    # FUNCTION: hardy_weinberg
    # input = p: allele requency of the dominant allele
    # output = q (recessive): the frequencies of the three genotypes (fAA, fAB, fBB)
    q <- 1 - p
  
    print(sum(c(q,p)))


}
##########################################
# END FUNCTION

hardy_weinberg()




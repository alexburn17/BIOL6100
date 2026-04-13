# GLM LECTURE
# P. Alexander Burnham
# 5 April 2026

# read in libraries
library(dplyr)
library(ggplot2)
library(stringr)
library(tidyr)
library(car)
library(lme4)


# Read Data in
dat_long <- read.csv("data/Burnham_field_data_pathogens_wide.csv", header=TRUE, stringsAsFactors=FALSE, comment.char="#")



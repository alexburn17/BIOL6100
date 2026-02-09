# Logistic Growth and Functions
# Solution to homework 5
# P. Alexander Burnham
# 4 February 2026


# Begin Creating Functions Here
#----------------------------------------------------#



# LOGISTIC GROWTH FUNCITON
######################################################
logistic_growth <- function(
  N0 = 10,      # initial population
  r  = 0.3,     # growth rate
  K  = 100,     # carrying capacity
  t_max = 50,   # end time
  dt = 0.1      # timestep
){
  
  # time vector
  time <- seq(0, t_max, by = dt)
  
  # logistic equation
  N <- K / (1 + ((K - N0) / N0) * exp(-r * time))
  
  # return tidy dataframe
  data.frame(
    time = time,
    population = N,
    N0 = N0,
    r = r,
    K = K
  )
}
######################################################
# END FUNCTION


######################################################
growth_plotter <- function(data){

  library(ggplot2)
  
  ggplot(df, aes(x = time, y = population)) +
    geom_line(size = 1.2) +
    labs(
      title = "Logistic Growth Model",
      x = "Time",
      y = "Population Size"
    ) +
    theme_minimal(base_size = 17)
}
######################################################




# Driver Section of Script
#----------------------------------------------------#

# run the model with required parms
df <- logistic_growth(
  N0 = 5,
  r  = 0.25,
  K  = 200,
  t_max = 60
)

# plot the output df
growth_plotter(data = df)









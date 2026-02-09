# Logistic Growth and Functions
# Solution to homework 5
# P. Alexander Burnham
# 4 February 2026


# Begin Creating Functions Here
#----------------------------------------------------#



# LOGISTIC GROWTH FUNCTION
######################################################
# Function Name: logistic_growth
#
# Purpose:
#   Simulates continuous-time logistic population growth using the
#   closed-form solution to the logistic differential equation.
#   Returns a tidy dataframe suitable for plotting or further analysis.
#
# Inputs:
#   N0 (numeric)  : Initial population size at time t = 0
#   r  (numeric)  : Intrinsic growth rate
#   K  (numeric)  : Carrying capacity
#   t_max (numeric) : Maximum simulation time
#   dt (numeric)  : Time step used to generate the time vector
#
# Output:
#   data.frame containing:
#     time (numeric)        : Time values from 0 to t_max
#     population (numeric)  : Population size N(t) at each time
#     N0 (numeric)          : Initial population parameter used
#     r (numeric)           : Growth rate parameter used
#     K (numeric)           : Carrying capacity parameter used
######################################################
logistic_growth <- function(
  N0 = 10,
  r  = 0.3,
  K  = 100,
  t_max = 50,
  dt = 0.1
){
  
  # time vector
  time <- seq(0, t_max, by = dt)
  
  # logistic equation (closed-form solution)
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



# PLOTTING FUNCTION
######################################################
# Function Name: growth_plotter
#
# Purpose:
#   Creates a ggplot visualization of population growth over time
#   using the dataframe produced by logistic_growth().
#
# Inputs:
#   data (data.frame) :
#     Must contain columns named:
#       time (numeric)
#       population (numeric)
#
# Output:
#   ggplot object showing population vs time.
#   The plot is printed to the plotting window.
######################################################
growth_plotter <- function(data){

  library(ggplot2)
  
  ggplot(data, aes(x = time, y = population)) +
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


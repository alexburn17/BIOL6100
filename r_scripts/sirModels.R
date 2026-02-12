library(deSolve)

#----------------------------------------------------#
# FUNCTION NAME: run_sir_model
#
# PURPOSE:
# Runs a deterministic SIR (Susceptible–Infectious–Recovered)
# epidemiological model using the deSolve ODE solver and
# returns the simulated epidemic time series as a data frame.
#
# INPUTS:
# beta    : numeric
#           Transmission rate (per contact per time step)
#
# gamma   : numeric
#           Recovery rate (per time step)
#
# N       : numeric
#           Total population size
#
# S0      : numeric
#           Initial number of susceptible individuals
#
# I0      : numeric
#           Initial number of infectious individuals
#
# R0      : numeric
#           Initial number of recovered individuals
#
# t_start : numeric
#           Start time of simulation
#
# t_end   : numeric
#           End time of simulation
#
# dt      : numeric
#           Time step size
#
# OUTPUT:
# A data.frame containing:
#   time : numeric vector of time steps
#   S    : susceptible population at each time step
#   I    : infectious population at each time step
#   R    : recovered population at each time step
#----------------------------------------------------#

run_sir_model <- function(
  beta    = 0.1,
  gamma   = 0.1,
  N       = 1000,
  S0      = 999,
  I0      = 1,
  R0      = 0,
  t_start = 0,
  t_end   = 160,
  dt      = 1
) {

  # Initial state vector
  init <- c(S = S0, I = I0, R = R0)

  # Time vector
  times <- seq(t_start, t_end, by = dt)

  #----------------------------------------------------#
  # FUNCTION NAME: sir_equations
  #
  # PURPOSE:
  # Defines the system of differential equations for the
  # SIR epidemiological model.
  #
  # INPUTS:
  # time       : numeric time step (required by deSolve)
  # state      : named vector of state variables (S, I, R)
  # parameters : named vector containing beta, gamma, N
  #
  # OUTPUT:
  # List containing derivatives:
  #   dS/dt, dI/dt, dR/dt
  #----------------------------------------------------#
  sir_equations <- function(time, state, parameters) {
    with(as.list(c(state, parameters)), {
      dS <- -beta * S * I / N
      dI <-  beta * S * I / N - gamma * I
      dR <-  gamma * I

      list(c(dS, dI, dR))
    })
  }

  # Run ODE solver
  out <- ode(
    y     = init,
    times = times,
    func  = sir_equations,
    parms = c(beta = beta, gamma = gamma, N = N)
  )

  # Convert to data frame
  out <- as.data.frame(out)

  return(out)
}

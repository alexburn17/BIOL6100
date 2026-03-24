# Homework 6
---
###For Loops and SIR Parameter Sweep
**P. Alexander Burnham**		
**10 February 2026**


-


#### 1) Create a function that takes as its inputs, vectors for $\beta$ (the transmission rate) and $\gamma$ (the recovery rate). This function will output a dataframe that includes the max number of infected individuals for each parameter combination.

A parameter sweep is done to explore the parameter space of a model by running a simulation for many combinations of parameters within a realistic range. Here we will do this for the SIR model. The equations for the classic SIR (Susceptible, Infected, and Recovered) model are below...


$$
\begin{align}
\frac{dS}{dt} &= -\beta \frac{SI}{N} \\
\frac{dI}{dt} &= \beta \frac{SI}{N} - \gamma I \\
\frac{dR}{dt} &= \gamma I
\end{align}$$

Where...

$$\begin{align}
N &= S + I + R
\end{align}$$

And the paramters are defined as...

$$\begin{align*}
S(t) &: \text{Number of susceptible individuals} \\
I(t) &: \text{Number of infected individuals} \\
R(t) &: \text{Number of recovered individuals} \\
N &= S + I + R \quad \text{(total population)} \\
\beta &: \text{Transmission rate} \\
\gamma &: \text{Recovery rate}
\end{align*}$$


This set of ordinary differential equations in their current form cannot be solved for (i.e. there is no closed form solution) so we will need to solve them numerically. To do this, we will use the `deSolve` package. This package inludes a number of numerical integration methods to solve for a system of ODEs. Make sure it is installed before sourcing it with `library(deSolve)`.

**Biological Motavation:** A key quantity in infectious disease dynamics is the basic reproduction number, $R_0=\beta/\gamma$, which represents the average number of secondary infections caused by one infectious individual in a fully susceptible population. Epidemics grow when $R_0 > 1$ and die out when $R_0 < 1$ By sweeping across values of $\beta$ and $\gamma$, this exercise lets you visualize how epidemic size changes across regions of parameter space.

The function below solves the SIR model for a single parameter set and will be used inside your loops to conduct the parameter sweep.

```r
library(deSolve)

############################################################
# FUNCTION: run_sir_model
# PURPOSE: Solve deterministic SIR model with deSolve
# INPUTS:
#   beta, gamma : transmission & recovery rates
#   N           : total population
#   S0, I0, R0  : initial conditions
#   t_start     : start time
#   t_end       : end time
#   dt          : timestep
# OUTPUT:
#   data.frame with columns: time, S, I, R
############################################################

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

  init  <- c(S = S0, I = I0, R = R0)
  times <- seq(t_start, t_end, by = dt)

  sir_equations <- function(time, state, parameters) {
    with(as.list(c(state, parameters)), {
      dS <- -beta * S * I / N
      dI <-  beta * S * I / N - gamma * I
      dR <-  gamma * I
      list(c(dS, dI, dR))
    })
  }

  out <- ode(
    y     = init,
    times = times,
    func  = sir_equations,
    parms = c(beta = beta, gamma = gamma, N = N)
  )

  as.data.frame(out)
}

```

To achieve this goal, you will need to create a container to store your results in your function (a data frame of the appropriate length of empty varaibles). This data frame will have columns for max_infected, beta, and gamma. In your script, create vectors of $\beta$ and $\gamma$ values ranging from 0 to 0.5 in steps of 0.01. Pass these vectors into your function.

Your nested for loop will be contained within your function and inside both loops, you will run the `run_sir_model` function. Your returned data frame of max infected values will be used in the next question.


--

#### 2) Create a second function that takes the above outputted dataframe as its input and creates a heatmap of max(number of infected) with $Transmission \ Rate, \beta$ and $Recovery \ Rate, \gamma$ as your $x$ and $y$ axises.

This function will take your data frame as input. The output will be the above mentioned plot, which can be created and styled in any way you want and with any plotting software availble in R.


-
#### Hints...

* When indexing into your empty dataframe to store your results, you will find that a nested for loop structure is naturally set up to store results in a matrix. However, plotting software in R prefers a data frame to create a heat map. For row indexing, it may be helpful to set up a counter that increases by 1 as it goes through both loops. Something like this...

```R
counter <- 1

loop 1{
	loop 2{
	
		x <- Do Things
		df <- Store Things		
		counter <- counter + 1 # increase your counter for the next round
	}
}

```

* Your container (storage data frame) should have the same number of rows as the length of `length(beta_vec)` $*$ `length(gamma_vec)`.
* Note: Including zero values for $\beta$ and $\gamma$ produces biologically meaningful edge cases where the infection never spreads. In your plot you may see stripes that are entirely max infection values of 0. This is expected.
* The rest of the parameters are fixed in the model as defaults but may also be changed. play around with population size and total time of the simulation. For some values of $\beta$ and $\gamma$ the full dynamics may not be captured by the default time length.





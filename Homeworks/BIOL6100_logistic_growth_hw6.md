# Homework 5
---
###Functions and The Logistic Growth Model
**P. Alexander Burnham**		
**4 February 2026**


-

#### 1) Create a function that takes the parameters required to run a logistic growth model and returns a dataframe with columns for population size and time.

The differential equation describing this process is below...

$$\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$$

If you recall, the closed form solution to this differential equation requires an initial condition for population size, $N_0$ and gives you a value for the population size at any given time, $N(t)$. This equation will be the one you code in your function.
$$
N(t) = \frac{K}{1 + \left(\frac{K - N_0}{N_0}\right)e^{-rt}}
$$


To get you started, I will list below the inputs your function will require to work properly.

* The initial population size, $N_0$
* The growth rate, $r$
* The carrying capacity, $K$
* The end time for your time vector, $t_{final}$
* The timestep for your time vector, $t_{step}$

You should not need any global variables to do this. Keep all parameters as local within your function. The final step is to return your dataframe for plotting.

--

#### 2) Create a second function that takes the above dataframe as its input and creates a plot of population size over time as a side effect.

The hard part is over. Now you just need to create a second function that takes your dataframe and creates a plot. You can use ggplot or base graphics to do so. Remember to add meaningful axis labels. Now, you should be able to run your model and create a plot with different parameter sets by running only 2 lines of code.



-
#### Hints...

* Look up any mathmatical operators we haven't covered explicitly in class. Ensure that parentheses and numerators/denominators are correctly possition to capture the equation. This should be achievable with one line of code.
* Remember to resource your function evertime you make a change or the function in memory will not include that change.
* Since we are not solving the differential equation directly/numerically (i.e. with a package like `desolve`), we need to have a vector of times over which to evaluate this equation. Use your parameters to create your time vector within the function. 
* Remeber to add comments within your function listing the name, parameters, their required variable types/meaning, outputs, and overall purpose of the function.






w
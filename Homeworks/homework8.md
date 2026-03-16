# Computational Biology 6100 - Homework 8
---
###Visualizing Statistical Designs with ggplot
**P. Alexander Burnham**		
**11 March 2026**

-

In this assignment we will create figures in ggplot corresponding to the four major statistical designs involving relationships of the form, $y \sim x$.

Different combinations of **continuous** and **discrete** variables lead to different statistical methods and different styles of visualization.

Your task is to generate figures in **ggplot2** that appropriately represent each type of relationship.

---

## Statistical Designs for $y \sim x$

| X Variable Type | Y Variable Type | Statistical Design              | Typical Analysis                                              | Resulting Figure                            |
| --------------- | --------------- | ------------------------------- | ------------------------------------------------------------- | ------------------------------------------- |
| Continuous      | Continuous      | Correlation / Linear Regression | Fit a linear model describing how (y) changes with (x)        | Scatter plot with regression line           |
| Discrete        | Continuous      | ANOVA (or other group comparison test)                | Compare means of (y) among groups defined by (x)              | Boxplot, violin plot, or barplot                      |
| Continuous      | Discrete        | Logistic Regression             | Model probability of category membership as a function of (x) | Scatter plot (jittered) with logistic curve |
| Discrete        | Discrete        | Contingency Analysis ($\chi^2$ test for independence)            | Examine association between two categorical variables         | Bar plot or mosaic plot                     |

---

## General Instructions

For each question:

1. Use a dataset of your choice:
 * 	`iris` or `car` datasets
 *  simulate your own dataset
 *  use a dataset of your own/from your work
 *  use a dataset included on the [BIOL6100 web page](https://alexburn17.github.io/BIOL6100/Datasets/Example_Datasets.html)
2. Produce a **ggplot figure** that appropriately visualizes the relationship for each question.
3. Label axes and include an informative title.
4. Use clear plotting aesthetics.

---

# Questions

---

## Question 1: Continuous (x), Continuous (y)

Use a dataset where both **x and y are continuous variables**.

For example, (y) could depend linearly on (x) with some noise.

Your figure should:

* Display the relationship between the variables
* Include a **fitted regression line**

**Required figure**

* Scatter plot of (y) vs (x)
* Regression line using `geom_smooth(method = "lm")`

---

## Question 2: Discrete (x), Continuous (y)

Use a dataset where:

* (x) is a **categorical variable** representing groups (e.g., treatment A/B/C)
* (y) is **continuous**

Your figure should show the distribution of (y) for each category.

**Required figure (choose 1):**

* OPTION 1:
	* Boxplot or violin plot
	* Points overlaid using jitter (`geom_jitter()`)
* OPTION 2:
	* Barplot with error bars
	* Summarize relationships with dplyr or similar

---

## Question 3: Continuous (x), Discrete (y)

Use a dataset where:

* (x) is **continuous**
* (y) is **binary** (0/1) 

*HINT: If you don't have a binary variable, create one by descritizing a continuous variable using a threathold, or encode a two factor catagorical variable as binary.*

Your figure should illustrate how the **probability of (y=1)** changes with (x).

**Required figure**

* Jittered points
* Logistic regression curve using `geom_smooth(method = "glm", method.args = list(family = "binomial"))`

---

## Question 4: Discrete (x), Discrete (y)

Use a dataset where both variables are **categorical**.

For example:

* (x): treatment group
* (y): outcome category

Your figure should display the counts or proportions of outcomes for each group.

**Required figure (choose 1)**

* OPTION 1:
	* Bar plot showing counts or proportions
* OPTION 2:
	* Mosaic plot 	

---


# Homework 14
---
### Multivariate Analysis 
**P. Alexander Burnham**		
**14 April 2026**


---

## Assignment:
#### Using a dataset of your choice, create a random forest model and a PCA to answer some questions about the data.

## Datasets:
#### You can do this assignment with a data set of your choice: 

* Any of the datasets linked at the top of the class website
* The wide-form bumble bee disease dataset
* Gapminder, cars
* Your own dataset 


## PCA:

**Conduct a PCA, and ansswer the following questions:**

* Create a figure showing PC1 and PC2 with 95% CI ellipses 
	* Do you see good separation of your groups on either axis?     	
* Based on a scree plot and broken stick test how many PCs are needed?
	* How much variance is explained by PC1 and PC2?
* Conduct a significance test. Is there a difference between groups?
* Based on the loadings, what variables are contributing the most to PC1 and PC2?

*Hint: `pca$rotation` will give the matrix with loadings for each variable for each PC.* 	


## Random Forest:

**Conduct a random forrest model with the same data set:**

* What is your OOB?
* Based on your confusion matrix, how accurate was your model at classifying?     	
* What variables were most important based on:
	* Mean Decrease Accuracy
	* Mean Decrease Gini 	

## Summary:

* Did your two models agree or disagree on variable importance?
* What differences did you notice based on the two approaches.


## Output:

#### Please post an html of your work with a section for each question/hypothesis you tested. Each section should include:
* The dataset you used
* The code and output of your model, significance test, and figures
* The answers to the questions for each model.  

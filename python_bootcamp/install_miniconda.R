# INTRO TO PYTHON
# MAY 4, 2023
# P. Alexander Burnham
# Installing Reticulate and Miniconda

# install and load reticulate
install.packages("reticulate")
library(reticulate)

# install miniconda
install_miniconda(path = miniconda_path(), update = TRUE, force = TRUE)


conda_install("r-reticulate", "numpy")
conda_install("r-reticulate", "pandas")
conda_install("r-reticulate", "scipy")
conda_install("r-reticulate", "matplotlib")
conda_install("r-reticulate", "statsmodels")
conda_install("r-reticulate", "seaborn")





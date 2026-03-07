# Supervised Machine Learning Regression Project

## Project Title
Sales Prediction using Machine Learning on Blinkit Dataset

## Problem Statement

The objective of this project is to predict product sales using supervised machine learning regression models based on product and outlet features.

## Dataset Description

The project uses the Blinkit Grocery Sales dataset which contains information about product characteristics and outlet details.
The target variable is **Sales**, which represents the total sales value of a product.

Main features include:

* Item Fat Content
* Item Weight
* Item Visibility
* Item Type
* Outlet Size
* Outlet Location Type
* Outlet Type
* Rating
* Sales (Target Variable)

## Data Cleaning and Preprocessing

The following preprocessing steps were performed:

* Handling missing values
* Fixing data types
* Removing duplicate records
* Detecting and treating outliers
* Removing irrelevant features (Item Identifier, Outlet Identifier)
* Encoding categorical variables using One-Hot Encoding
* Applying feature scaling using StandardScaler
* Splitting the dataset into training and testing sets
* Transforming skewed features where necessary

## Algorithms Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

## Evaluation Metrics

The models were evaluated using:

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)

## Conclusion

Among the three models, Random Forest provided better prediction performance due to its ensemble learning capability.

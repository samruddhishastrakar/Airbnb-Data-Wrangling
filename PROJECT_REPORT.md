# Mini Project Report

## Airbnb Data Wrangling using Python and Streamlit

### 1. Introduction

Data wrangling is the process of collecting, cleaning and preparing data
for analysis. In this project, Airbnb listing data is processed using
simple Python programs and displayed through a Streamlit application.

The project demonstrates how Airbnb data can be loaded, inspected,
cleaned and visualized using Python, Pandas, Matplotlib and Streamlit.

### 2. Objectives

- Load Airbnb data.
- Understand the dataset.
- Find missing values.
- Remove duplicate records.
- Fill missing values.
- Analyze Airbnb price categories.
- Compare average prices across property types.
- Compare average prices across locations.
- Create basic visualizations.

### 3. Technologies Used

Python, Pandas, Matplotlib and Streamlit.

### 4. Dataset

The Airbnb dataset contains the following columns:

- Airbnb_ID
- Property_Type
- Room_Type
- Location
- Price_Per_Night
- Minimum_Nights
- Number_of_Reviews
- Review_Score

These variables provide information about Airbnb listings,
their prices, locations, property types and guest reviews.

### 5. Data Cleaning

The following operations are performed:

1. Duplicate records are removed.
2. Missing Price Per Night values are replaced by the mean.
3. Missing Minimum Nights values are replaced by the median.
4. Missing Number of Reviews values are replaced by the median.
5. Missing Review Score values are replaced by the mean.
6. Missing Property Type values are replaced by the mode.
7. Missing Room Type values are replaced by the mode.
8. Missing Location values are replaced by the mode.

### 6. Airbnb Price Analysis

Instead of Pass/Fail class balancing, the project analyzes Airbnb
price categories.

The listings are divided into four categories:

- Budget
- Moderate
- Premium
- Luxury

The project also calculates and compares average Airbnb prices
for different property types and locations.

### 7. Visualization

The project creates:

- Airbnb Property Type distribution bar chart
- Price Per Night histogram
- Price vs Number of Reviews scatter plot
- Price vs Review Score scatter plot
- Average Price by Location bar chart

These visualizations help understand the distribution and relationships
within the Airbnb dataset.

### 8. Learning Outcomes

After completing this project, students can:

- Read CSV files using Pandas.
- Inspect an Airbnb dataset.
- Find missing values.
- Remove duplicate records.
- Fill missing values using mean, median and mode.
- Create categories using Pandas.
- Calculate average prices using groupby().
- Create basic charts.
- Build a simple Streamlit application.

### 9. Conclusion

This project provides a beginner-friendly introduction to data wrangling
using Airbnb listing data.

It demonstrates how raw Airbnb data can be loaded, cleaned, analyzed
and visualized using simple Python commands and a Streamlit application.

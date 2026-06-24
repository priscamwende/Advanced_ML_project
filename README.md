# Advanced_ML_project

# Individual Household Electric Power Consumption Forecasting Using Advanced Machine Learning Models

## Project Overview

This project focuses on analyzing and forecasting household electricity consumption using advanced machine learning and time series forecasting techniques. The dataset contains measurements of electric power consumption collected from a single household over several years, providing valuable insights into energy usage patterns and enabling the prediction of future electricity demand.

The project explores both traditional statistical forecasting methods and modern machine learning approaches to evaluate their effectiveness in predicting energy consumption.



## Objectives

The primary objectives of this project are to:

- Analyze household electricity consumption patterns.
- Perform exploratory data analysis and feature engineering.
- Apply dimensionality reduction techniques to identify important features.
- Discover hidden consumption patterns using clustering algorithms.
- Forecast future electricity consumption using classical time series models.
- Compare traditional forecasting techniques with deep learning approaches.
- Evaluate model performance using appropriate forecasting metrics.



## Dataset Description

### Dataset Name

**Individual Household Electric Power Consumption Dataset**

### Dataset Characteristics

The dataset contains measurements collected between December 2006 and November 2010 at a one-minute sampling rate.

### Features

| Feature | Description |
|----------|------------|
| Date | Date of observation |
| Time | Time of observation |
| Global_active_power | Household global active power (kilowatts) |
| Global_reactive_power | Household global reactive power (kilowatts) |
| Voltage | Voltage (volts) |
| Global_intensity | Current intensity (amperes) |
| Sub_metering_1 | Kitchen energy consumption |
| Sub_metering_2 | Laundry room energy consumption |
| Sub_metering_3 | Water heater and air conditioner energy consumption |

### Target Variable

**Global Active Power**



# Methodology

## 1. Data Preprocessing

The following preprocessing steps were performed:

- Handling missing values
- Converting date and time columns into datetime format
- Resampling data into hourly or daily intervals
- Feature scaling and normalization
- Creating lag features for time series forecasting

## 2. Exploratory Data Analysis (EDA)

The dataset was analyzed to identify:

- Daily electricity consumption trends
- Weekly and seasonal patterns
- Peak energy usage periods
- Correlations among electrical variables
- Distribution of power consumption values

### Visualizations

- Time series plots
- Correlation heatmaps
- Distribution plots
- Seasonal decomposition plots



## 3. Dimensionality Reduction

### Principal Component Analysis (PCA)

PCA was applied to:

- Reduce feature dimensionality
- Eliminate redundant information
- Improve computational efficiency
- Visualize feature relationships

### Kernel PCA

Kernel PCA was used to capture nonlinear relationships within the electrical measurements.



## 4. Clustering Analysis

Unsupervised learning techniques were employed to identify consumption patterns.

### K-Means Clustering

Used to group periods with similar energy consumption behavior.

### Hierarchical Clustering

Applied to explore hierarchical relationships between energy usage profiles.

### Gaussian Mixture Models (GMM)

Used to identify probabilistic clusters and overlapping consumption patterns.

### Kernel Density Estimation (KDE)

Used to estimate the probability distribution of electricity consumption values.



## 5. Time Series Forecasting

### ARIMA

AutoRegressive Integrated Moving Average was used to model non-seasonal consumption patterns.

### SARIMA

Seasonal ARIMA was implemented to capture recurring seasonal behavior.

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Akaike Information Criterion (AIC)
- Bayesian Information Criterion (BIC)



## 6. Deep Learning Models

### Artificial Neural Network (ANN)

A feedforward neural network was developed for electricity consumption prediction.

### Recurrent Neural Network (RNN)

RNN architecture was implemented to capture temporal dependencies.

### Long Short-Term Memory (LSTM)

LSTM networks were used to model long-term sequential patterns in electricity consumption data.



# Model Comparison

| Model | Category |
|---------|---------|
| ARIMA | Statistical |
| SARIMA | Statistical |
| ANN | Deep Learning |
| RNN | Deep Learning |
| LSTM | Deep Learning |

Models were compared based on:

- Forecasting accuracy
- Error metrics
- Computational efficiency
- Ability to capture seasonality

# Technologies Used

## Programming Language

- Python

## Libraries

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Machine Learning

- Scikit-Learn

### Time Series Analysis

- Statsmodels
- pmdarima

### Deep Learning

- TensorFlow
- Keras

# Evaluation Metrics

## Mean Absolute Error (MAE)

Measures the average magnitude of prediction errors.

## Root Mean Squared Error (RMSE)

Measures the standard deviation of prediction errors.

## R² Score

Measures the proportion of variance explained by the model.

## Akaike Information Criterion (AIC)

Used for model selection among ARIMA-family models.

## Bayesian Information Criterion (BIC)

Used to evaluate model complexity and goodness of fit.


# Expected Outcomes

This project aims to:

- Accurately forecast future household electricity consumption.
- Identify hidden patterns in energy usage behavior.
- Compare classical time series methods with deep learning techniques.
- Provide insights that support energy management and demand planning.


# Future Improvements

Potential future enhancements include:

- Incorporating weather data
- Integrating smart meter data from multiple households
- Implementing Transformer-based forecasting models
- Real-time energy demand prediction
- Energy anomaly detection


# Conclusion

This project demonstrates the application of advanced machine learning, unsupervised learning, time series analysis, and deep learning techniques to household electricity consumption forecasting. By comparing statistical and neural network approaches, the study provides insights into the strengths and limitations of various forecasting methods and contributes toward intelligent energy management systems.



Advanced Machine Learning Project

Household Electricity Consumption Forecasting and Pattern Analysis using Machine Learning and Deep Learning Models.

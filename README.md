# Household Electricity Consumption Forecasting Using Machine Learning and Deep Learning

##  Project Overview

This project develops an end-to-end electricity consumption forecasting system using both **Machine Learning** and **Deep Learning** techniques. The objective is to accurately predict **Global Active Power** consumption by first identifying electricity consumption patterns through clustering and then training forecasting models on engineered time-series features.

The project combines:
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Dimensionality reduction
- Clustering
- Artificial Neural Networks (ANN)
- Long Short-Term Memory (LSTM)


## Dataset

The project uses the **Individual Household Electric Power Consumption** dataset.

The dataset contains household electricity measurements including:

- Global Active Power
- Global Reactive Power
- Voltage
- Global Intensity
- Sub-metering 1
- Sub-metering 2
- Sub-metering 3

The original minute-level data was aggregated into **hourly observations** for forecasting.



#  Project Workflow

## 1. Data Preprocessing

The preprocessing stage included:

- Loading the dataset
- Combining Date and Time columns
- Converting to datetime format
- Setting datetime as the index
- Handling missing values
- Removing invalid observations
- Resampling the data into hourly intervals

---

## 2. Exploratory Data Analysis (EDA)

The dataset was explored using:

- Missing value analysis
- Summary statistics
- Histograms
- Boxplots
- Correlation heatmaps
- Time series visualizations

This helped understand consumption patterns and detect outliers.



## 3. Feature Scaling

RobustScaler was applied to normalize the numerical variables while reducing the effect of outliers.



## 4. Dimensionality Reduction

Two dimensionality reduction techniques were implemented:

- Principal Component Analysis (PCA)
- Kernel PCA

These methods were used to:

- Reduce redundancy
- Improve clustering
- Visualize high-dimensional data



## 5. Clustering

Three clustering algorithms were evaluated:

- K-Means
- Hierarchical Clustering
- Gaussian Mixture Model (GMM)

The models were compared using:

- Silhouette Score
- Calinski-Harabasz Index
- Davies-Bouldin Index

K-Means achieved the best clustering performance and was selected as the final clustering algorithm.

The resulting clusters represented different electricity consumption regimes:

- Low Consumption
- Medium Consumption
- High Consumption

## 6. Feature Engineering

Additional predictive variables were created.

### Time Features

- Hour
- Day
- Month
- Day of Week

### Lag Features

Historical electricity consumption values were included:

- lag1
- lag2
- lag3
- lag24

These lag variables enable the forecasting models to learn historical consumption patterns.

## 7. Forecasting Models

### Artificial Neural Network (ANN)

The ANN model learns nonlinear relationships between the engineered features and electricity consumption.

### Long Short-Term Memory (LSTM)

The LSTM model is specifically designed for time-series forecasting and captures temporal dependencies in electricity consumption.

#  Model Evaluation

The forecasting models were evaluated using:

### Mean Absolute Error (MAE)

- Lower values indicate better prediction accuracy.
- Measures the average prediction error.

### Root Mean Squared Error (RMSE)

- Lower values indicate better performance.
- Penalizes larger prediction errors more heavily.

### Coefficient of Determination (R²)

- Higher values indicate better performance.
- Measures how well the model explains the variability in electricity consumption.

#  Results

| Model | MAE | RMSE | R² |
|-------|------:|------:|------:|
| ANN | 0.079372 | 0.109230 | 0.977501 |
| **LSTM** | **0.019101** | **0.029317** | **0.998379** |

##  Best Model

The **LSTM** achieved the best forecasting performance because it produced:

- The lowest Mean Absolute Error (MAE)
- The lowest Root Mean Squared Error (RMSE)
- The highest R² score

This demonstrates that LSTM is more effective than ANN for forecasting household electricity consumption.


# Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
tensorflow
keras
scipy
```



#  Project Pipeline

```
Data Loading
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Scaling
      │
      ▼
PCA & Kernel PCA
      │
      ▼
K-Means Clustering
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
ANN Model
      │
      ▼
LSTM Model
      │
      ▼
Model Evaluation
      │
      ▼
Model Comparison
```



#  Conclusion

This project presents a complete machine learning pipeline for forecasting household electricity consumption.

By combining clustering, feature engineering, and deep learning, highly accurate electricity consumption forecasts were achieved. Both ANN and LSTM models were trained and evaluated, with the LSTM consistently outperforming the ANN across all evaluation metrics. The findings demonstrate that LSTM is well suited for time-series forecasting due to its ability to learn temporal dependencies in sequential data.





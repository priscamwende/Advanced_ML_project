# Household Electricity Consumption Profiling and Forecasting
### **Project Overview**

This project develops an end-to-end household electricity consumption analysis and forecasting system using Machine Learning and Time Series Forecasting techniques. The objective is to identify household electricity consumption patterns through clustering and accurately forecast future Global Active Power consumption using a Seasonal ARIMA (SARIMA) model.

**The project combines:**

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature scaling
- Dimensionality reduction
- Clustering
- Time series forecasting
- Interactive Streamlit deployment

**Dataset**

The project uses the Individual Household Electric Power Consumption dataset.

The dataset contains household electricity measurements including:

* Global Active Power
* Global Reactive Power
* Voltage
* Global Intensity
* Sub-metering 1
* Sub-metering 2
* Sub-metering 3

The original minute-level data was aggregated into hourly observations for clustering and forecasting.

#### **Project Workflow**
***1. Data Preprocessing***

The preprocessing stage included:

* Loading the dataset
*  Combining Date and Time columns
*  Converting to datetime format
*  Setting datetime as the index
*  Handling missing values
*  Removing invalid observations
*  Resampling the data into hourly intervals

2. ***Exploratory Data Analysis (EDA)***

The dataset was explored using:

* Missing value analysis
* Summary statistics
* Histograms
* Boxplots
* Correlation heatmaps
* Time-series visualizations

This helped identify consumption trends, seasonal patterns, and potential outliers.

***3. Feature Scaling***

StandardScaler was applied to standardize all numerical variables before dimensionality reduction and clustering. This ensured that features measured on different scales contributed equally to the analysis.

***4. Dimensionality Reduction***

Two dimensionality reduction techniques were implemented:

* Principal Component Analysis (PCA)
* Kernel PCA

These methods were used to:

* Reduce feature redundancy
* Capture nonlinear relationships
* Improve clustering performance
* Visualize high-dimensional data
  
***5. Clustering***

Three clustering algorithms were evaluated:

* K-Means
* Hierarchical Clustering
* Gaussian Mixture Model (GMM)

The clustering models were compared using:

* Silhouette Score
* Calinski-Harabasz Index
* Davies-Bouldin Index

*K-Means achieved the best overall performance and was selected as the final clustering model.*

The resulting household consumption regimes were:

- Very Low
- Low
- Low-Medium
- Medium
- High
  
***6. Time Series Forecasting***

A Seasonal ARIMA (SARIMA) model was developed to forecast future Global Active Power consumption.

*The forecasting workflow included:*

* Stationarity testing
* Seasonal decomposition
* Model selection
* Residual diagnostics
* Future electricity demand prediction
* Model Evaluation

The forecasting model was evaluated using:

- Mean Absolute Error (MAE)
Measures the average prediction error.

- Root Mean Squared Error (RMSE)
Measures prediction accuracy while giving greater weight to larger errors.

- Coefficient of Determination (R²)
Measures how well the model explains the variation in electricity consumption.

Residual diagnostics, including histogram, Q-Q plot, and autocorrelation analysis, were also performed to assess model adequacy.

### Results

**Clustering**

K-Means produced the best clustering performance among the evaluated algorithms.
Households were successfully grouped into five meaningful electricity consumption regimes.
The resulting clusters support customer segmentation and personalized energy management.

**Forecasting**
The SARIMA model successfully captured both trend and seasonality in household electricity consumption.
Residual diagnostics indicated that the model adequately explained the temporal structure of the data.
The forecasting model can be used to estimate future electricity demand and support energy planning.

#### Libraries Used

- pandas
- numpy
- matplotlib
- scikit-learn
- statsmodels
- joblib
- streamlit
- reportlab

#### Project Pipeline

Data Loading
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Scaling (StandardScaler)
      │
      ▼
PCA & Kernel PCA
      │
      ▼
Cluster Evaluation
      │
      ▼
K-Means Clustering
      │
      ▼
Household Consumption Profiling
      │
      ▼
Time Series Analysis
      │
      ▼
SARIMA Forecasting
      │
      ▼
Model Evaluation
      │
      ▼
Streamlit Deployment

#### **Streamlit Application**

The project includes an interactive Streamlit application with two modules:

**Household Consumption Profiling**

Users can:

1. Enter household electricity measurements.
2. Predict the household's electricity consumption regime.
3. View personalized interpretations and energy-saving recommendations.
4. Download a PDF report.

**Electricity Forecasting**

Users can:

1. Generate future electricity consumption forecasts.
2. Visualize predicted electricity demand.
3. Download forecast results as a CSV file.
   
### **Business Value**

The project helps electricity providers:

1. Understand household electricity consumption behaviour.
2. Forecast future electricity demand more accurately.
3. Improve energy planning and resource allocation.
4. Design targeted energy efficiency programs.
5. Enhance grid reliability through data-driven decision-making.

#### **Conclusion**

This project presents a complete machine learning and time series forecasting framework for household electricity consumption analysis. By combining PCA, Kernel PCA, K-Means clustering, and SARIMA forecasting, the project successfully identifies household consumption regimes and predicts future electricity demand. The accompanying Streamlit application makes these insights accessible through an interactive interface, supporting smarter energy management and operational decision-making.




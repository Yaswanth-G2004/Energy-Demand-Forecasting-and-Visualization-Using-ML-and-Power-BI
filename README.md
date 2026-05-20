# Energy Demand Forecasting and Visualization Using Machine Learning and Power BI

## Project Overview
This project focuses on forecasting electricity energy demand using Machine Learning techniques and visualizing insights through Power BI dashboards. The system analyzes historical energy production and consumption data from different sources such as biomass, fossil fuels, hydro, nuclear, solar, and wind energy.

The project helps in predicting future energy demand and supports better energy management and decision-making.

---

## Features

- Forecasts future energy demand using Machine Learning models
- Real-time prediction using Flask web application
- Power BI dashboard for data visualization and analysis
- Comparison of multiple energy sources
- Cost and consumption analysis
- User-friendly interface for predictions

---

## Technologies Used

### Programming Languages
- Python
- SQL
- HTML
- CSS
- JavaScript

### Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- Matplotlib
- Seaborn

### Tools
- Power BI
- VS Code
- Jupyter Notebook

---

## Machine Learning Models Used

1. XGBoost Regressor  
2. Random Forest Regressor  

The performance of both models was evaluated, and XGBoost provided better prediction accuracy.

---

## Dataset Details

The dataset contains historical energy demand and production records from multiple energy sources:

- Biomass
- Fossil Gas
- Fossil Hard Coal
- Hydro Energy
- Nuclear Energy
- Solar Energy
- Wind Energy

The dataset was preprocessed to remove missing values and generate lag features for time-series forecasting.

---

## System Architecture

1. Data Collection  
2. Data Preprocessing  
3. Feature Engineering  
4. Model Training  
5. Energy Demand Prediction  
6. Visualization using Power BI  
7. Real-time Prediction using Flask Application  

---

## Project Workflow

### Step 1: Data Preprocessing
- Cleaned missing and null values
- Converted date and time columns
- Created lag features for forecasting

### Step 2: Model Training
- Trained Random Forest Regressor
- Trained XGBoost Regressor
- Compared model performance using evaluation metrics

### Step 3: Prediction
- Generated future energy demand predictions
- Integrated predictions into Flask application

### Step 4: Visualization
- Created interactive Power BI dashboards
- Visualized energy consumption trends and cost analysis

---

## Evaluation Metrics

The following metrics were used to evaluate model performance:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Power BI Dashboard Features

- Energy source comparison
- Monthly and yearly energy trends
- Cost analysis visualization
- Demand forecasting charts
- Interactive filters and reports

---

## Flask Web Application

The Flask application allows users to:

- Enter input values
- Predict future energy demand
- View real-time prediction results

---

## Future Enhancements

- Integration with live IoT energy data
- Deep Learning models for improved accuracy
- Cloud deployment
- Mobile application support
- Real-time analytics dashboard

---

## Project Outcome

This project successfully predicts future energy demand using Machine Learning models and provides interactive visualizations through Power BI. The system helps improve energy planning and resource management.

---

## Author

Garikipati Yaswanth  
B.Tech – Computer Science Engineering

---

## License

This project is developed for academic and educational purposes.

# 🚗 AutoPrice AI – Automobile Price Prediction

An end-to-end Machine Learning project that predicts the selling price of used cars based on their specifications using Linear Regression.

## 🌐 Live Demo

🚀 **Try the Application:**  
[AutoPrice AI – Live Streamlit App](https://autoprice-ai-automobile-price-prediction-smfdhdwwyfa229edqjr34.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://autoprice-ai-automobile-price-prediction-smfdhdwwyfa229edqjr34.streamlit.app/)

## 📌 Project Overview

The Automobile Price Prediction project uses Machine Learning to estimate the selling price of used cars.

The application takes car details such as brand, manufacturing year, fuel type, transmission, mileage, engine capacity, and other specifications as input.

Based on these details, the trained Linear Regression model predicts the estimated selling price.

## 🎯 Project Objectives

- Predict used car selling prices.
- Understand the factors affecting automobile prices.
- Perform data cleaning and preprocessing.
- Analyze automobile data using EDA.
- Build a Machine Learning regression model.
- Develop an interactive web application using Streamlit.
- Deploy the application online.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Algorithm:** Linear Regression
- **Model Tuning:** GridSearchCV
- **Model Deployment:** Streamlit Community Cloud
- **Model Saving:** Joblib
- **Development Environment:** Jupyter Notebook, VS Code

## 📂 Dataset Information

The dataset contains automobile specifications and their selling prices.

### Features Used

| Feature | Description |
|---|---|
| Brand | Car manufacturer |
| Year | Manufacturing year |
| Fuel_Type | Fuel category |
| Transmission | Manual or Automatic |
| Owner_Type | Number/type of previous owners |
| Body_Type | Vehicle body category |
| Kilometers_Driven | Distance driven |
| Mileage | Fuel efficiency |
| Engine_CC | Engine capacity |
| Max_Power_BHP | Maximum engine power |
| Seats | Seating capacity |

**Target Variable:** `Selling_Price_Lakh`

## ⚙️ Project Workflow

1. Dataset Collection
2. Data Understanding
3. Data Cleaning
4. Handling Missing Values
5. Exploratory Data Analysis (EDA)
6. Categorical Feature Encoding
7. Feature Preprocessing
8. Train-Test Split
9. Linear Regression Model Training
10. Hyperparameter Tuning using GridSearchCV
11. Model Evaluation
12. Model Saving using Joblib
13. Streamlit Web Application Development
14. Deployment using Streamlit Community Cloud

## 🤖 Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict continuous numerical values.

In this project, Linear Regression is used to estimate the selling price of used automobiles based on their features.

## 📊 Model Evaluation Metrics

The following metrics can be used to evaluate the regression model:

- **MAE:** Mean Absolute Error
- **MSE:** Mean Squared Error
- **RMSE:** Root Mean Squared Error
- **R² Score:** Measures how well the model explains price variations.

*Add your actual evaluation results here after checking your notebook.*

## 💻 Application Features

- Interactive Streamlit interface.
- Car brand selection.
- Vehicle specification inputs.
- Automated price prediction.
- User-friendly prediction results.
- Online application access.

## 📸 Application Preview

Visit the live application to explore the interface and test car price predictions.

🔗 [Open AutoPrice AI](https://autoprice-ai-automobile-price-prediction-smfdhdwwyfa229edqjr34.streamlit.app/)

## 📁 Project Structure

```text
AutoPrice-AI-Automobile-Price-Prediction/
│
├── app.py
├── automobile_linear_regression_tuned.pkl
├── car_background_streamlit.jpg
├── prediction_dataset.csv
├── AutoPrice_AI_Automobile-Price-Prediction.ipynb
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the project folder

```bash
cd AutoPrice-AI-Automobile-Price-Prediction
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```bash
streamlit run app.py
```

## 🔮 Future Improvements

- Explore additional real-world automobile datasets.
- Improve prediction accuracy through feature engineering.
- Compare Linear Regression with other regression algorithms.
- Add more automobile brands and specifications.
- Improve the user interface and visualization.
- Deploy improved versions of the application.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Data preprocessing and cleaning.
- Exploratory Data Analysis.
- Feature encoding and scaling.
- Regression model development.
- Model evaluation and tuning.
- Streamlit application development.
- Machine Learning model deployment.

## 👨‍💻 Author

**Nidigallu Sandeep**

Aspiring Data Scientist | Machine Learning Enthusiast

🔗 **GitHub:** [My GitHub Profile](https://github.com/nidigallusandeep-arch)

🔗 **Live Project:** [AutoPrice AI](https://autoprice-ai-automobile-price-prediction-smfdhdwwyfa229edqjr34.streamlit.app/)

---

⭐ If you find this project useful, feel free to explore and give it a star!

**Note:** The predicted price is an estimate generated from the trained model and dataset. It is not a guaranteed real-world market price.

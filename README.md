Climate Change Prediction

Overview

This project focuses on predicting extreme weather conditions, such as precipitation and wind speed, using a Machine Learning model. A Random Forest Regressor is employed for the prediction task. Additionally, a Streamlit web application is developed to allow users to input climate parameters manually and receive predictions.

Features

Data Preprocessing: Cleaning and preparing climate data for training.

Machine Learning Model: Uses a Random Forest Regressor for prediction.

Web Application: A Streamlit-based interactive UI for easy model usage.

Performance Evaluation: Model performance is assessed using evaluation metrics such as RMSE.

Installation

Prerequisites

Ensure you have Python installed on your system.

Clone the Repository

git clone https://github.com/musadiq044/climate_change_prediction.git
cd climate_change_prediction

Install Dependencies

pip install -r requirements.txt

Usage

Train the Model

Run the script to train the model:

python train_model.py

Run the Web App

Launch the Streamlit application using:

streamlit run app.py

File Structure

climate_change_prediction/
│── data/                   # Dataset files
│── models/                 # Trained models
│── app.py                  # Streamlit web app
│── train_model.py          # Model training script
│── requirements.txt        # Dependencies
│── README.md               # Project documentation

Future Improvements

Integrating more weather parameters for better predictions.

Implementing additional machine learning models for comparison.

Enhancing the Streamlit UI for better user experience.

Contributing

Feel free to fork this repository, make enhancements, and submit pull requests.

License

This project is licensed under the MIT License.

Author: Musadiq044

For any inquiries, please open an issue in the repository.

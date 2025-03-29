import streamlit as st
import numpy as np
import pickle

# Load the trained models
with open("gb_model_precip.pkl", "rb") as file:
    model_precip = pickle.load(file)

with open("gb_model_wind.pkl", "rb") as file:
    model_wind = pickle.load(file)

# Streamlit App UI
st.title("🌍 Climate Change Prediction App")

st.write("Enter the following values to predict **Precipitation (mm)** and **Wind Speed (m/s)**.")

# User Input
year = st.number_input("Year", min_value=1900, max_value=2100, value=2025)
month = st.number_input("Month", min_value=1, max_value=12, value=6)
avg_temp = st.number_input("Avg Temperature (°C)", value=25.0)
max_temp = st.number_input("Max Temperature (°C)", value=30.0)
min_temp = st.number_input("Min Temperature (°C)", value=20.0)
humidity = st.number_input("Humidity (%)", value=60.0)
solar_irradiance = st.number_input("Solar Irradiance (W/m²)", value=200.0)
cloud_cover = st.number_input("Cloud Cover (%)", value=50.0)
co2_conc = st.number_input("CO2 Concentration (ppm)", value=400.0)
latitude = st.number_input("Latitude", value=35.0)
longitude = st.number_input("Longitude", value=80.0)
altitude = st.number_input("Altitude (m)", value=100.0)
proximity_water = st.number_input("Proximity to Water (km)", value=10.0)
urbanization = st.number_input("Urbanization Index", value=0.5)
vegetation = st.number_input("Vegetation Index", value=0.6)
enso_index = st.number_input("ENSO Index", value=0.0)
particulate_matter = st.number_input("Particulate Matter (µg/m³)", value=35.0)
sea_surface_temp = st.number_input("Sea Surface Temperature (°C)", value=25.0)

# Prepare input for prediction
input_features = np.array([[year, month, avg_temp, max_temp, min_temp, humidity,
                            solar_irradiance, cloud_cover, co2_conc, latitude, longitude,
                            altitude, proximity_water, urbanization, vegetation,
                            enso_index, particulate_matter, sea_surface_temp]])

# Predict
if st.button("Predict"):
    precip_prediction = model_precip.predict(input_features)[0]
    wind_prediction = model_wind.predict(input_features)[0]

    st.subheader("🌧️ Predicted Precipitation:")
    st.write(f"**{precip_prediction:.2f} mm**")

    st.subheader("💨 Predicted Wind Speed:")
    st.write(f"**{wind_prediction:.2f} m/s**")

st.write("Developed By Musadiq Surya Siranjeevi**")

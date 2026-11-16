import joblib
import pandas as pd
import streamlit as st

 
# Cache the model so it doesn't reload on every user interaction
@st.cache_resource
def load_model():
    return joblib.load('/Users/cheikh/Documents/Projects/House Price Prediction/model_RFR.pkl')
  
    
#1. Functions 
def disable_button():
    st.session_state.is_disabled = True
    
def enable_button():
    st.session_state.is_disabled = False

def is_in_range(value, min_val, max_val):
    return min_val <= value and value <= max_val
        
def validate_renovation_year():
    year_built = st.session_state.yr_built
    year_renovated = st.session_state.yr_renovated

    if year_renovated != None and year_renovated <= year_built:
        st.toast("⚠️ Warning: The year of the renovations cannot be before the year in which the house was built. Please enter a valid input.", icon="🚨")
        disable_button()
    else:
        enable_button()

def validate_area_size(rooms):
    for size in rooms:
        if not is_in_range(size, 300, 15000):
            return False
    return True
    
def validate_dates(year):
    return year == None or is_in_range(year, 1900, 2015)
    
if "is_disabled" not in st.session_state:
    st.session_state.is_disabled = False
    
model = load_model()


# 2. App Title and Description
st.title("King County House Value Predictor")
st.text("This app allows users to generate a quote for a home in King County, USA based off of a Random Forest Regression machine learning model. \nAdjust the house specifications below to predict its price. \nArea measurements are limited from 300 sq. ft. to 15 000 sq. ft. \nDates (Year Built & Year Renovated) are restricted from 1900 to 2015.")


# 3. Input Widgets
bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=8, value=3)
bathrooms = st.slider("Number of Bathrooms", min_value=1, max_value=8, value=2)
sqft_living = st.number_input("Living Area (sq ft)", value=1500)
sqft_lot = st.number_input("Lot Area (sq ft)", value=1500)
floors = st.slider("Floors", min_value=1, max_value=4, value=2)
waterfront_active = st.toggle("Waterfront", value=False)
waterfront = int(waterfront_active)
view = st.slider("View", min_value=0, max_value=4, value=1)
condition = st.slider("Condition", min_value=1, max_value=5, value=1)
grade = st.slider("Grade", min_value=1, max_value=13, value=1)
sqft_above = st.number_input("Area Above (sq ft)", value=1500)
sqft_basement = st.number_input("Basement (sq ft)", value=500)
yr_built = st.number_input("Year Built", value=2005, key="yr_built")
yr_renovated = st.number_input("Year Renovated", value=None, step=1, key="yr_renovated", on_change=validate_renovation_year)
zipcode = st.slider("Zipcode", min_value=98001, max_value=98199, value=98001)
lat = st.slider("Latitude", min_value=47.0, max_value=48.0, value=47.1559, step=0.0001)
long = st.slider("Longitude", min_value=-123.0, max_value=-121.0, value=-122.519, step=0.001)
sqft_living15 = st.number_input("Living Area 2015 (sq ft)", value=1500)
sqft_lot15 = st.number_input("Lot Area 2015 (sq ft)", value=1500)

rooms = [sqft_living, sqft_lot, sqft_above, sqft_basement, sqft_living15, sqft_lot15]


# 4. Format Inputs and Prediction
if st.button("Predict Price", disabled=st.session_state.is_disabled):
    input_data = pd.DataFrame({
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms], 
        "sqft_living": [sqft_living], 
        "sqft_lot": [sqft_lot],
        "floors": [floors],
        "waterfront": [waterfront],
        "view": [view],
        "condition": [condition],
        "grade": [grade],
        "sqft_above": [sqft_above],
        "sqft_basement": [sqft_basement],
        "yr_built": [yr_built],
        "yr_renovated": [yr_renovated],
        "zipcode": [zipcode],
        "lat": [lat],
        "long": [long],
        "sqft_living15": [sqft_living15],
        "sqft_lot15": [sqft_lot15]
    })
    
    if validate_area_size(rooms):
        if validate_dates(yr_built) and validate_dates(yr_renovated):
                prediction = model.predict(input_data)[0]
                st.success(f"Estimated House Price: ${prediction:,.2f}")
        else:
            st.error("One of the date fields has a value that is not within the allowed range (1900 to 2015).")    
    else:
        st.error("One of the area fields has a value that is not within the allowed range (300 to 15000 sq. ft).")
     
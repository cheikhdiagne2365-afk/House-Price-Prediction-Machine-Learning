# House Price Prediction (Machine Learning)
Machine Learning Project with the goal of training several regression models to predict the price of sale for houses based on a database of real estate sales in King County, Washington, USA between the years of 1900 and 2015. 

Original Database: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

## Columns
- id
- date
- price
- bedrooms
- bathrooms
- sqft_living
- sqft_lot
- floors
- waterfront
- view
- condition
- grade
- sqft_above
- sqft_basement
- yr_built
- yr_renovated
- zipcode
- lat (Latitude)
- long (Longitude)
- sqft_living15
- sqft_lot15

## How to Install Streamlit
1. Ensure that your device has Python (version 3.10 to 3.14) and pip installed
2. Create a virtual environment by running this command:
  ```
  python -m venv .venv
  ```
3. Activate the virtual environment using this command:
  ```
  Windows: .venv\Scripts\activate
  MacOS/Linux: source .venv/bin/activate
  ```
4. Run the pip installation command for Streamlit:
  ```
  pip install streamlit
  ```
5. Verify that Streamlit has been properly installed by running the built-in demo app:
  ```
  streamlit hello
  ```

## How to Run The Application
Once Streamlit has been installed onto your computer, follow these steps to be able to use the House Price Predictor Application.

1. Clone the repository into your terminal or download it as a zip file
2. Once the repository is cloned/downloaded, open a terminal for the folder
     - Windows: Open the folder, right-click an empty space, and select Open in Terminal (Windows 11). On older versions, hold Shift, right-click, and select Open PowerShell window here or Open command window here.
     - MacOS: Right-click the desired folder in Finder and select New Terminal at Folder.
     - Linux: Open your file manager, right-click inside the folder, and select Open in Terminal.
3. Once the terminal is open in the desired folder, run this command to start the app:
  ```
  streamlit run app.py
  ```

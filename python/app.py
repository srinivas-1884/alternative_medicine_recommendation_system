import streamlit as st
import pickle
import time
import pandas as pd
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Application Backend
@st.cache_data
def load_medicines():
    # Load the Excel file
    medicine_description_path = 'Medicine_description.xlsx'
    medicines = pd.read_excel(medicine_description_path)
    return medicines

@st.cache_data
def load_similarity():
    # Load similarity-vector-data from pickle in the form of dictionary
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return similarity

medicines = load_medicines()
similarity = load_similarity()

def recommend(medicine):
    try:
        medicine_index = medicines[medicines['Name'] == medicine].index[0]
    except IndexError:
        st.error("Medicine not found. Please check the name and try again.")
        return []

    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Name)
    return recommended_medicines

# Application Frontend

# Title of the Application
st.title('Alternate Medicine Recommendation System')

# Searchbox
selected_medicine_name = st.selectbox(
    'Type the Medicine Name For Alternate Medicine',
    [''] + list(medicines['Name'].values),  # Include an empty string as the first option
)

# Recommendation Program
if st.button('Recommend Medicine'):
    if selected_medicine_name != '':
        with st.spinner('Fetching recommendations...'):
            time.sleep(5)
            recommendations = recommend(selected_medicine_name)
        if recommendations:
            for j, medicine_name in enumerate(recommendations, start=1):
                medicine_info = medicines[medicines['Name'] == medicine_name].iloc[0]
                st.write(f"{j}. {medicine_name}")
                st.write(f"   - Description: {medicine_info['Description']}")
                st.write(f"   - Manufacturer: {medicine_info['Manufacturer Name']}")

                st.write("   - Buy Here:")
                st.write(f"       - [PharmEasy](https://pharmeasy.in/search/all?name={medicine_name})")
                st.write(f"       - [1mg](https://www.1mg.com/search/all?name={medicine_name})")
                st.write(f"       - [Apollo](https://www.apollopharmacy.in/search-medicines/{medicine_name})")
                st.markdown("---")
    else:
        st.warning("Please select a medicine.")

# Load and display an image for the app
image = Image.open('0_KxyYRO0zTAcAeHss.jpg')
st.image(image, caption='Recommended Medicines')

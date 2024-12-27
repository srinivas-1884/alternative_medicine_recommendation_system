# Alternative Medicine System
The Alternate Medicine Recommendation System helps users find alternative medications by inputting a specific medicine name. It provides a list of substitutes with detailed information, using data analysis and similarity algorithms. This tool improves access, addresses medication availability, cost, and awareness, enhancing healthcare convenience.
Installation and Usage Guide
Installation
To set up and run the application locally, follow these steps:

1. Clone the Repository
Execute the following commands to download the project and navigate to its directory:

code:
git clone https://github.com/your-username/alternate-medicine-recommendation-system.git  
cd alternate-medicine-recommendation-system  

2. Install Dependencies
Ensure you have Python 3.x installed, then install the required packages by running:

code:
pip install -r requirements.txt  
The requirements.txt file should include the following packages:

streamlit
pandas
pickle-mixin
scikit-learn
numpy
pillow

3. Start the Application
Run the Streamlit server with the command:

code:
streamlit run app.py  

*** Usage ***
1. Upload Data Files
Ensure the following files are placed in the root directory:

Medicine_description.xlsx
similarity.pkl

2. Search for Medicines
Use the dropdown menus to filter by Type and Manufacturer.
Select a specific medicine to view its alternatives.

3. Get Recommendations
Click the Recommend Medicine button to display alternative medicines. Each recommendation includes:

Description: Key details about the alternative medicine.
Price: If price data is available.
Manufacturer: Information about the manufacturer.
Direct Links: Purchase options on platforms like PharmEasy, 1mg, and Apollo.
Image: A picture of the medicine (if available).

4. Interactive Display
The app enhances user experience by providing:

Images of the medicines.
Direct purchasing links for convenience.

This application is designed to simplify the process of finding alternative medicines and making informed choices.

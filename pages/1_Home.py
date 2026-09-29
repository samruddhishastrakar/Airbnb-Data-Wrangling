import streamlit as st

st.title("🏠 1. Home")

st.header("Airbnb Data Wrangling")

st.write("""
Data wrangling means preparing raw data so that it can be used for
analysis. In this project, we use an Airbnb dataset and perform simple
data-wrangling operations.
""")

st.subheader("Project Objectives")

st.write("1. Load a CSV file using Pandas.")
st.write("2. Check the number of rows and columns.")
st.write("3. Find missing values.")
st.write("4. Remove duplicate records.")
st.write("5. Fill missing values.")
st.write("6. Understand the distribution of Airbnb listings.")
st.write("7. Analyze Airbnb prices and reviews.")
st.write("8. Create basic charts.")

st.subheader("Dataset Columns")

st.table({
    "Column": [
        "Airbnb_ID",
        "Property_Type",
        "Room_Type",
        "Location",
        "Price_Per_Night",
        "Minimum_Nights",
        "Number_of_Reviews",
        "Review_Score"
    ],
    "Meaning": [
        "Unique Airbnb listing number",
        "Type of property",
        "Type of room offered",
        "Location of the Airbnb",
        "Price charged per night",
        "Minimum number of nights required",
        "Total number of reviews received",
        "Average rating given by guests"
    ]
})

st.success("Go to Page 2 to load and inspect the Airbnb data.")

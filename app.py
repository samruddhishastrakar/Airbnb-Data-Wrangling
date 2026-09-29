import streamlit as st

st.set_page_config(
    page_title="Airbnb Data Wrangling",
    page_icon="🏠"
)

st.title("🏠 Airbnb Data Wrangling")

st.write(
    "A simple beginner project using Python, Pandas and Streamlit."
)

st.subheader("What will we learn?")

st.write("""
This project shows the basic steps of data wrangling:

1. Load Airbnb data
2. Understand the data
3. Clean the data
4. Analyze Airbnb prices
5. Create charts
""")

st.info(
    "Use the pages in the left sidebar to go through the project step by step."
)

st.subheader("Tools Used")

st.write("• Python")
st.write("• Pandas")
st.write("• Matplotlib")
st.write("• Streamlit")

st.subheader("Project Dataset")

st.write("""
The dataset contains Airbnb listing information such as property type,
room type, location, price per night, minimum nights, number of reviews
and review score.
""")

st.subheader("Project Workflow")

st.write("""
🏠 Load Data → 🧹 Clean Data → ⚖️ Analyze Prices → 📊 Create Charts
""")

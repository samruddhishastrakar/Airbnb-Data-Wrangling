import streamlit as st
import pandas as pd

st.title("📂 2. Load and Understand Airbnb Data")

uploaded_file = st.file_uploader("Upload an Airbnb CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/airbnb_data.csv")
    st.info("Using the sample airbnb_data.csv file.")

st.subheader("First 10 Airbnb Records")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Number of Rows and Columns")

col1, col2 = st.columns(2)
col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

st.subheader("Column Names")
st.write(list(df.columns))

st.subheader("Data Types")
st.write(df.dtypes)

st.subheader("Missing Values")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.subheader("Basic Statistics")
st.dataframe(df.describe(), use_container_width=True)

st.subheader("Number of Duplicate Rows")
st.write(df.duplicated().sum())

st.success("Now go to Page 3 to clean the Airbnb data.")

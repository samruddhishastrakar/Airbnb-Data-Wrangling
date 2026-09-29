import streamlit as st
import pandas as pd

st.title("🧹 3. Clean Airbnb Data")

df = pd.read_csv("data/airbnb_data.csv")

st.subheader("Before Cleaning")

st.write("Missing values:")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.write("Duplicate rows:", df.duplicated().sum())

st.subheader("Step 1: Remove Duplicate Rows")

df = df.drop_duplicates()

st.write("Rows after removing duplicates:", len(df))

st.subheader("Step 2: Fill Missing Values")

# Fill missing Price Per Night with the average
df["Price_Per_Night"] = df["Price_Per_Night"].fillna(
    df["Price_Per_Night"].mean()
)

# Fill missing Minimum Nights with the median
df["Minimum_Nights"] = df["Minimum_Nights"].fillna(
    df["Minimum_Nights"].median()
)

# Fill missing Number of Reviews with the median
df["Number_of_Reviews"] = df["Number_of_Reviews"].fillna(
    df["Number_of_Reviews"].median()
)

# Fill missing Review Score with the average
df["Review_Score"] = df["Review_Score"].fillna(
    df["Review_Score"].mean()
)

# Fill missing Property Type with the most common value
df["Property_Type"] = df["Property_Type"].fillna(
    df["Property_Type"].mode()[0]
)

# Fill missing Room Type with the most common value
df["Room_Type"] = df["Room_Type"].fillna(
    df["Room_Type"].mode()[0]
)

# Fill missing Location with the most common value
df["Location"] = df["Location"].fillna(
    df["Location"].mode()[0]
)

st.write("Missing values after cleaning:")
st.dataframe(df.isnull().sum().to_frame("Missing Values"))

st.subheader("Cleaned Airbnb Data")
st.dataframe(df, use_container_width=True)

st.success("Cleaning completed!")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Cleaned Airbnb Data",
    csv,
    "cleaned_airbnb_data.csv",
    "text/csv"
)

st.info("""
### What did we do?

* Removed duplicate rows using drop_duplicates()

* Filled missing Price Per Night using the mean

* Filled missing Minimum Nights using the median

* Filled missing Number of Reviews using the median

* Filled missing Review Score using the mean

* Filled categorical missing values using the mode
""")

import streamlit as st
import pandas as pd

st.title("⚖️ 4. Airbnb Price Analysis")

df = pd.read_csv("data/airbnb_data.csv")

# Clean the data first
df = df.drop_duplicates()

df["Price_Per_Night"] = df["Price_Per_Night"].fillna(
    df["Price_Per_Night"].mean()
)

df["Minimum_Nights"] = df["Minimum_Nights"].fillna(
    df["Minimum_Nights"].median()
)

df["Number_of_Reviews"] = df["Number_of_Reviews"].fillna(
    df["Number_of_Reviews"].median()
)

df["Review_Score"] = df["Review_Score"].fillna(
    df["Review_Score"].mean()
)

df["Property_Type"] = df["Property_Type"].fillna(
    df["Property_Type"].mode()[0]
)

df["Room_Type"] = df["Room_Type"].fillna(
    df["Room_Type"].mode()[0]
)

df["Location"] = df["Location"].fillna(
    df["Location"].mode()[0]
)

st.subheader("Step 1: Analyze Price Distribution")

st.write(df["Price_Per_Night"].describe())

st.subheader("Step 2: Create Price Categories")

# Create price categories
df["Price_Category"] = pd.cut(
    df["Price_Per_Night"],
    bins=[0, 2500, 5000, 7500, float("inf")],
    labels=["Budget", "Moderate", "Premium", "Luxury"]
)

price_count = df["Price_Category"].value_counts().sort_index()

st.write(price_count)

st.bar_chart(price_count)

st.subheader("Step 3: Average Price by Property Type")

average_price = df.groupby("Property_Type")["Price_Per_Night"].mean()

st.dataframe(
    average_price.reset_index().rename(
        columns={"Price_Per_Night": "Average Price"}
    ),
    use_container_width=True
)

st.bar_chart(average_price)

st.subheader("Step 4: Average Price by Location")

location_price = df.groupby("Location")["Price_Per_Night"].mean()

st.dataframe(
    location_price.reset_index().rename(
        columns={"Price_Per_Night": "Average Price"}
    ),
    use_container_width=True
)

st.bar_chart(location_price)

st.subheader("Airbnb Data with Price Categories")

st.dataframe(df.head(20), use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Airbnb Analysis Data",
    csv,
    "airbnb_analysis_data.csv",
    "text/csv"
)

st.success("Airbnb price analysis completed!")

st.info("""
### What did we do?

* Removed duplicate Airbnb listings

* Filled missing values

* Created four price categories:
  Budget, Moderate, Premium and Luxury

* Compared average prices across property types

* Compared average prices across locations
""")

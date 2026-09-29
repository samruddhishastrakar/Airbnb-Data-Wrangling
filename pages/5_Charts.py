import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 5. Airbnb Data Visualization")

df = pd.read_csv("data/airbnb_data.csv")

# Simple cleaning
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

# --------------------------------------------------
# 1. Property Type Distribution
# --------------------------------------------------

st.subheader("1. Airbnb Property Type Distribution")

property_count = df["Property_Type"].value_counts()

fig, ax = plt.subplots()

property_count.plot(kind="bar", ax=ax)

ax.set_xlabel("Property Type")
ax.set_ylabel("Number of Listings")
ax.set_title("Airbnb Listings by Property Type")

st.pyplot(fig)


# --------------------------------------------------
# 2. Price Per Night Distribution
# --------------------------------------------------

st.subheader("2. Price Per Night Distribution")

fig, ax = plt.subplots()

ax.hist(df["Price_Per_Night"], bins=10)

ax.set_xlabel("Price Per Night")
ax.set_ylabel("Number of Listings")
ax.set_title("Airbnb Price Distribution")

st.pyplot(fig)


# --------------------------------------------------
# 3. Price vs Number of Reviews
# --------------------------------------------------

st.subheader("3. Price vs Number of Reviews")

fig, ax = plt.subplots()

ax.scatter(
    df["Price_Per_Night"],
    df["Number_of_Reviews"]
)

ax.set_xlabel("Price Per Night")
ax.set_ylabel("Number of Reviews")
ax.set_title("Price vs Number of Reviews")

st.pyplot(fig)


# --------------------------------------------------
# 4. Price vs Review Score
# --------------------------------------------------

st.subheader("4. Price vs Review Score")

fig, ax = plt.subplots()

ax.scatter(
    df["Price_Per_Night"],
    df["Review_Score"]
)

ax.set_xlabel("Price Per Night")
ax.set_ylabel("Review Score")
ax.set_title("Price vs Review Score")

st.pyplot(fig)


# --------------------------------------------------
# 5. Average Price by Location
# --------------------------------------------------

st.subheader("5. Average Price by Location")

location_price = (
    df.groupby("Location")["Price_Per_Night"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()

location_price.plot(kind="bar", ax=ax)

ax.set_xlabel("Location")
ax.set_ylabel("Average Price Per Night")
ax.set_title("Average Airbnb Price by Location")

st.pyplot(fig)


# --------------------------------------------------
# Simple Observations
# --------------------------------------------------

st.subheader("Simple Observations")

st.write(
    "• The bar chart shows the distribution of Airbnb listings across property types."
)

st.write(
    "• The histogram shows how Airbnb prices are distributed."
)

st.write(
    "• The first scatter plot helps us understand the relationship between price and number of reviews."
)

st.write(
    "• The second scatter plot helps us understand the relationship between price and review score."
)

st.write(
    "• The location chart compares average Airbnb prices across different locations."
)

st.success(
    "Project completed! You have now performed a basic Airbnb data-wrangling and visualization workflow."
)

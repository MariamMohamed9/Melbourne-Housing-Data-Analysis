import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home", layout="wide")

html = """
<div style="text-align: center; color: white; font-size: 30px; font-weight: bold;">
    Melbourne House Prices EDA Project
</div>
"""
st.markdown(html, unsafe_allow_html=True)

df = pd.read_parquet("cleaned_data.parquet")

# عرض نموذج من البيانات
st.subheader("Data Overview")
st.dataframe(df)

# وصف الأعمدة
column_descriptions = {
    "Suburb": "Name of the suburb where the property is located",
    "Address": "Detailed address of the property",
    "Rooms": "Number of rooms in the property",
    "Type": "Property type (br: bedroom, h: house, t: townhouse, u: unit)",
    "Price": "Price of the property in AUD",
    "Method": "Method of sale (S: property sold, SP: property sold prior...)",
    "SellerG": "Real Estate Agent selling the property",
    "Date": "Date of sale",
    "Distance": "Distance from Central Business District (CBD) in kilometers",
    "Postcode": "Postal code of the area",
    "Bedroom2": "Scraped # of Bedrooms from different source",
    "Bathroom": "Number of Bathrooms",
    "Car": "Number of car spots",
    "Landsize": "Land Size in square meters",
    "BuildingArea": "Building Size in square meters",
    "YearBuilt": "Year the house was built",
    "CouncilArea": "Governing council for the area",
    "Regionname": "General Region (West, North West, North, etc.)",
    "Propertycount": "Number of properties that exist in the suburb",
}

description_df = pd.DataFrame(
    [
        {
            "Column": column,
            "Description": column_descriptions.get(
                column,
                "Description not available"
            )
        }
        for column in df.columns
        if not column.endswith("_id")
    ]
)

# Display title
st.subheader("📋 Dataset Column Descriptions")

# Display table
st.table(description_df)

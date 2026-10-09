
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Melbourne Housing Dashboard", page_icon="🏠", layout="wide"
)

html ="""
    <div style="text-align: center; color: white; font-size: 30px; font-weight: bold;">
        Melbourne House Prices EDA Project
    </div>
    """
st.markdown(
    "<h1 style='text-align: center;'>Melbourne House Prices EDA Project</h1>",
    unsafe_allow_html=True,
)

# Load Data
cleaned_df = pd.read_parquet("cleaned_data.parquet")

#Select Region
Regions_list=['All Regions'] + cleaned_df['Regionname'].unique().tolist()

Region=st.sidebar.multiselect('Region',Regions_list,default=['All Regions'])

if 'All Regions' not in Region:
    cleaned_df=cleaned_df[cleaned_df['Regionname'].isin(Region)]



#select Date
min_date = cleaned_df['Date'].min().date()
max_date = cleaned_df['Date'].max().date()


start_date = st.sidebar.date_input(
    'From',
    value=min_date,
    min_value=min_date,
    max_value=max_date)

end_date = st.sidebar.date_input(
    'To',
    value=max_date,
    min_value=min_date,
    max_value=max_date)



st.dataframe(cleaned_df)
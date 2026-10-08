
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

# Tabs
tab1, tab2 = st.tabs(['Numerical Analysis', 'Categorical Analysis'])

with tab1:
    st.subheader('Numerical Analysis')

with tab2:
    st.subheader('Categorical Analysis')
    num_cols = cleaned_df.select_dtypes(include= 'number').columns
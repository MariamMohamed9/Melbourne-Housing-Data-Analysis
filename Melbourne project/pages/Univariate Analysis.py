
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
    num_cols = cleaned_df.select_dtypes(include= 'number').columns
    col_select = st.selectbox('Select Column', num_cols)
    chart_select = st.radio('Select Chart Type', ['Histogram', 'Box Plot'])
    if chart_select == 'Histogram':
      st.plotly_chart(px.histogram(data_frame=cleaned_df, x=col_select, title=f'Histogram of {col_select}'))

    else:
      st.plotly_chart(px.box(data_frame=cleaned_df, x=col_select, title=f'Box Plot of {col_select}'))




with tab2:
    st.subheader('Categorical Analysis')
   
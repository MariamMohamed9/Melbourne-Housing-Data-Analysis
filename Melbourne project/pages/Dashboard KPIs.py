import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Melbourne Housing Dashboard", page_icon="🏠", layout="wide"
)

st.markdown("""
<style>
[data-testid="stMetricValue"] {
    font-size: 25px;
}
</style>
""", unsafe_allow_html=True)

html ="""
    <div style="text-align: center; color: white; font-size: 30px; font-weight: bold;">
        Melbourne House Prices EDA Project
    </div>
    """
st.markdown(
    "<h1 style='text-align: center;'>Melbourne House Prices EDA Project</h1>",
    unsafe_allow_html=True,)


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        "https://images.adsttc.com/media/images/6854/8198/8a40/7a01/8689/6242/newsletter/melbourne-architecture-city-guide-the-architectural-landmarks-that-make-one-of-the-worlds-most-liveable-cities_22.jpg?1750368681",
        width=600, 
        caption=None)

# Load Data
cleaned_df = pd.read_parquet("cleaned_data.parquet")

#numbers of sellers 
Total_sellers = cleaned_df['SellerG'].nunique()

#Total number of properties
suburb_per_region = (
    cleaned_df.groupby(["Regionname", "Suburb"])["Propertycount"]
    .first()
    .reset_index())

region_total_properties = ( suburb_per_region.groupby("Regionname")["Propertycount"].sum().astype(int))

grand_total_properties = region_total_properties.sum()

#Average price of properties in Melbourne
successful_sales = cleaned_df[cleaned_df["Method"].isin(["S", "SP", "SA"])]
overall_avg_price = round(successful_sales["Price"].mean(),2)

#Total Revenue from sold properties
sold_properties = cleaned_df[~cleaned_df['Method'].isin(['PI', 'W','VB'])]
total_revenue = sold_properties["Price"].sum().astype(int)


col1, col2, col3,col4 = st.columns(4)

with col1:
    st.metric(label="Total Sellers Agents", value=Total_sellers)

with col2:
    st.metric(label="Total Properties in Melbourne", value=grand_total_properties)

st.subheader("📌 Properties Breakdown by Region")

regions = region_total_properties.index

# نقسم الأقاليم على مجموعتين (كل مجموعة 4 أقاليم)
mid_point = len(regions) // 2
first_row_regions = regions[:mid_point]
second_row_regions = regions[mid_point:]

# الصف الأول (4 أعمدة)
cols1 = st.columns(len(first_row_regions))
for i, region in enumerate(first_row_regions):
  with cols1[i]:
    with st.container(border=True):
      prop_count = region_total_properties[region]
      st.metric(label=region, value=f"{prop_count:,}")

# الصف الثاني (باقي الأعمدة)
cols2 = st.columns(len(second_row_regions))
for i, region in enumerate(second_row_regions):
  with cols2[i]:
    with st.container(border=True):
      prop_count = region_total_properties[region]
      st.metric(label=region, value=f"{prop_count:,}")


with col3:
 st.metric(label="Average Price of Properties in Melbourne", value=f"AU${overall_avg_price:,}")

with col4:
 st.metric(label="Total Revenue ", value=f"AU${total_revenue:,}")

 #Total daily revenue from sold properties
Daily_revenue = (successful_sales.groupby('Date')['Price'] .sum().reset_index())
st.plotly_chart(px.line(data_frame=Daily_revenue,x='Date',y='Price',markers=True,
                        title='Daily Total Revenue over time',
                        labels={'Date':'Date','Price':'Total Revenue'}).update_layout(xaxis_title='Date',yaxis_title='Total Revenue (AUD)'))

#Total monthly revenue from sold properties
successful_sales['YearMonth'] = successful_sales['Date'].dt.strftime('%Y-%m')
monthly_revenue = successful_sales.groupby('YearMonth')['Price'].sum().reset_index()
st.plotly_chart(px.line(data_frame=monthly_revenue,
        x='YearMonth',
        y='Price',  
        labels={'YearMonth':'Month-Year', 'Price': 'Total Revenue'},
        markers=True,
        title='Monthly Total Revenue'
       ).update_layout(xaxis_title='Date', yaxis_title='Total Revenue (AUD)'))

#Total yearly revenue from sold properties
successful_sales['Year'] = successful_sales['Date'].dt.year.astype(str)
Annual_revenue = (successful_sales.groupby('Year')['Price'].sum().reset_index())

st.plotly_chart(px.line(data_frame=Annual_revenue,
        x='Year',
        y='Price',  
        labels={'Year': 'Year', 'Price': 'Total Revenue'},
        markers=True,
        title='Annual Total Revenue'
       ).update_layout(xaxis_title='Date', yaxis_title='Total Revenue (AUD)'))

# properties types
sold_properties = cleaned_df[~cleaned_df['Method'].isin(['PI', 'W','VB'])]
type_counts = sold_properties['Type'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']
st.plotly_chart(px.pie(data_frame=type_counts, names='Type', values='Count',title='Percentage of sold property types'))

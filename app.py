import streamlit as st
import plotly.graph_objects as go
import sidebar.overview as overview
import sidebar.about_dataset as about_dataset
import sidebar.market_insights as market_insights
import sidebar.brand_analysis as brand_analysis

st.set_page_config(
  layout = 'wide'
)



user_option = st.sidebar.selectbox('Choose',['Overview','Market Insights','Brand Analysis',"About Dataset"])

if user_option == 'Overview':
  overview.show()

elif user_option == 'Market Insights':
  market_insights.show()

elif user_option == 'Brand Analysis':
  brand_analysis.show()

elif user_option == 'About Dataset':
  about_dataset.show()

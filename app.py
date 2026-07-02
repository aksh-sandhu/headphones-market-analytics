import streamlit as st
import plotly.graph_objects as go
from sidebar import overview
from sidebar import about_dataset

st.set_page_config(
  layout = 'wide'
)



user_option = st.sidebar.selectbox('Choose',['Overview','Market Insights','Brand Analysis','Product Explorer',"About Dataset"])

if user_option == 'Overview':
  overview.show()

elif user_option == 'About Dataset':
  about_dataset.show()

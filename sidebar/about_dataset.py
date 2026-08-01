import streamlit as st
from database.queries import about_dataset_query
import pandas as pd
query = about_dataset_query()



def show():


   col1, col2, col3 = st.columns(3)

   with col1:
        st.metric('Number of Products:', query.total_products())

   with col2:
        st.metric("Total Brands", query.total_brands())

   with col3:
        st.metric("Database", "MySQL")

   col4, col5, col6 = st.columns(3)

   with col4:
        st.metric("Total Columns", query.total_columns())

   with col5:
        st.metric("Data Source", "Smartprix")

   with col6:
        st.metric("Data Type", "Headphones Dataset")




   st.header("About Dataset")
   st.markdown("""
   This dataset contains **1,020 headphone products** scraped from **Smartprix**.
   It includes product specifications such as price, rating, Bluetooth version,
   connectivity, microphone availability, fit type, and wireless range.
   The data was cleaned, transformed, and stored in MySQL before analysis.
   """)

   sample = st.empty()

   sample.dataframe(query.data_overview())

   if st.button("Random Sample"):
        sample.dataframe(query.button_pressed())









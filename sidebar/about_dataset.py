import streamlit as st
from database.queries import about_dataset_query
import pandas as pd
about_dataset_query = about_dataset_query()



def show():
   st.header("About Dataset",text_alignment = 'center')

   sample = st.empty()

   sample.dataframe(about_dataset_query.data_overview())

   if st.button("Random Sample"):
        sample.dataframe(about_dataset_query.button_pressed())





import streamlit as st
from database.queries import query
import pandas as pd
data = query()



def show():
   st.header("About Dataset",text_alignment = 'center')

   sample = st.empty()

   sample.dataframe(data.data_overview())

   if st.button("Random Sample"):
        sample.dataframe(data.button_pressed())


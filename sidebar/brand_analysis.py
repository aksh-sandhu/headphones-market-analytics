import streamlit as st
from database.connection import DB
from database.queries import brand_analysis_query
import utils.brand_analysis_charts as charts

db = DB()
brand_analysis_query = brand_analysis_query()

def show():

  with st.container():
    tot_brands,larg_brand,most_exp_brand,highest_rated_brand = st.columns(4,border=True)


    with tot_brands:
      st.write("Total Brands")
      total_brands = brand_analysis_query.total_brands()
      st.write(total_brands)

    with larg_brand:
      st.write('Largest Brand')
      name,count = brand_analysis_query.largest_brand()
      st.write(name,'',count)

    with most_exp_brand:
      st.write('Most Expensive Brand')
      brand,price = brand_analysis_query.most_expensive_brand()
      st.write(brand,'',price)


    with highest_rated_brand:
      pass



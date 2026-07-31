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
      st.write('Higest Rated Brand')
      company,star = brand_analysis_query.highest_rated()
      st.write(company,star,'⭐')


  top_count_fig = charts.top_company_count_chart()
  st.header('Top 15 Companies By Most Products',text_alignment='center')
  st.plotly_chart(top_count_fig)

  brand_list = brand_analysis_query.brand_list()
  user_option = st.selectbox('Choose Brand',brand_list)

  with st.container():

    product_count, connectivity, price_tiers = st.columns(3,border=True)

    with product_count:
      count_product = brand_analysis_query.selected_brand_count(user_option)
      st.header('Total Products',text_alignment='center')
      st.header(count_product,text_alignment='center')


    with connectivity:
      st.header('Connectivity Count',text_alignment='center')
      wireless,wired = brand_analysis_query.wireless_wired_count(user_option)
      wired_col,wireless_col = st.columns(2)
      with wired_col:
        st.write(f'Wirless Products: {wireless}')
      with wireless_col:
        st.write(f'Wired Products: {wired}')


    with price_tiers:
      budget,mid,premium,luxury = brand_analysis_query.price_tier_count(user_option)
      st.header('Price Tier Count',text_alignment='center')

      budget_cont,mid_cont = st.columns(2)
      with budget_cont:
        st.write(f'Budget Products: {budget}')
      with mid_cont:
        st.write(f'Mid Range Products: {mid}')

      premium_cont,luxury_cont = st.columns(2)
      with premium_cont:
        st.write(f'Premium Products: {premium}')
      with luxury_cont:
        st.write(f'Luxury Products: {luxury}')



    type_check, fit_type = st.columns(2,border=True)

    with type_check:
      # brand_analysis_query.microphone_check(user_option)
      fig = charts.type_check_chart(user_option)
      st.header('Type Percentage',text_alignment='center')
      st.plotly_chart(fig)

    with fit_type :
      pass





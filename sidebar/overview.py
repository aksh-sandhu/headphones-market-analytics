import streamlit as st
from database.connection import DB
from database.queries import overview_query
import utils.overview_charts as charts

st.set_page_config(
  layout = 'wide'
)

db = DB()
overview_query = overview_query()

def show():

  st.title("Headphones Market Analytics Dashboard (LIVE)")
  st.write('1020 Rows · scraped from Smartprix')
  with st.container():
    products,avg_price,avg_rating,brands = st.columns(4,border=True,width="stretch")

    with products:
      st.write('Total Products')
      product_count = overview_query.product_count()
      st.write(product_count)

    with avg_price:
      avg_price = overview_query.avg_price()
      st.write('Avg Price')
      st.write(f"₹ {avg_price:,.0f}")

    with avg_rating:
      avg_rating = overview_query.avg_rating()
      st.write('Avg Rating')
      st.write(avg_rating)

    with brands:
      brands = overview_query.total_company()
      st.write('Brands')
      st.write(brands)



    top_company,connectivity_share = st.columns(2,border=True)
    with top_company:
      fig = charts.top_count_company_chart()
      st.header('Top 20 Brand share',text_alignment='center')
      st.plotly_chart(fig)

    with connectivity_share:
      fig = charts.wired_wireless_chart()
      st.header('Wired vs Wireless',text_alignment='center')
      st.plotly_chart(fig)



    price_tier,top_avg_price = st.columns(2,border=True)
    with price_tier:
      fig = charts.price_tier_chart()
      st.header('Distribution Across Price Tiers',text_alignment='center')
      st.plotly_chart(fig)

    with top_avg_price:
      fig = charts.top_avg_price_chart()
      st.header('Brand Price Analysis',text_alignment='center')
      st.plotly_chart(fig)

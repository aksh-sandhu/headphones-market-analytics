import streamlit as st
import plotly.graph_objects as go
from database.connection import DB
from database.queries import query

st.set_page_config(
  layout = 'wide'
)

db = DB()
query = query()

def show():

  st.title("Headphones Market Analytics Dashboard (LIVE)")
  st.write('1020 Rows · scraped from Smartprix')
  with st.container():
    products,avg_price,avg_rating,brands = st.columns(4,border=True,width="stretch")

    with products:
      st.write('Total Products')
      product_count = query.product_count()
      st.write(product_count)

    with avg_price:
      avg_price = query.avg_price()
      st.write('Avg Price')
      st.write(f"₹ {avg_price:,.0f}")

    with avg_rating:
      avg_rating = query.avg_rating()
      st.write('Avg Rating')
      st.write(avg_rating)

    with brands:
      brands = query.total_company()
      st.write('Brands')
      st.write(brands)



    top_company,connectivity_share = st.columns(2,border=True)
    with top_company:
      company,count = query.top_count_company()
      fig = go.Figure(
        go.Pie(
          labels=company,
          values = count,
          hoverinfo='label+percent',
          textinfo='value'
        )
      )
      st.header('Top 20 Brand share',text_alignment='center')
      st.plotly_chart(fig)

    with connectivity_share:
      wireless = query.wireless_percent()
      wired = query.wired_percent()

      fig = go.Figure(
        go.Pie(
          labels = ['wireless','wired'],
          values = [wireless,wired],
          hole = 0.5,
          hoverinfo = 'label'
        )
      )
      st.header('Wired vs Wireless',text_alignment='center')
      st.plotly_chart(fig)



    price_tier,top_avg_price = st.columns(2,border=True)
    with price_tier:
      tier,count = query.price_tier()

      fig = go.Figure(
        go.Bar(
          x = tier,
          y = count,
          text=count,
          textposition = 'inside'
        )
      )
      fig.update_layout(
        title = 'Headphone Price Tier Distribution',
        xaxis_title = 'Segment',
        yaxis_title = 'count'
      )
      st.header('Distribution Across Price Tiers',text_alignment='center')
      st.plotly_chart(fig)

    with top_avg_price:
      company,avg_price = query.top_avg_price()
      fig = go.Figure(
        go.Bar(
          x = company,
          y = avg_price,
          text = avg_price,
          textposition = 'inside'
        )
      )
      fig.update_layout(
        title = 'Top 15 Brands by Average Headphone Price',
        xaxis_title = 'Brand',
        yaxis_title = 'Average Price'
      )
      st.header('Brand Price Analysis',text_alignment='center')
      st.plotly_chart(fig)

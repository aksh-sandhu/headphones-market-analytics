import streamlit as st
import utils.market_insights_charts as charts


def show():

  # budget,mid = st.columns(2,border=True)
  # with budget:
  #   fig_budget = charts.price_distribution_budget_histogram()
  #   st.header('Budget Tier Distribution Histogram',text_alignment='center')
  #   st.plotly_chart(fig_budget,key='budget')

  # with mid:
  #   fig_mid = charts.price_distribution_mid_histogram()
  #   st.header('Mid-Range Tier Distribution Histogram',text_alignment='center')
  #   st.plotly_chart(fig_mid,key='mid')

  # premium,luxury =  st.columns(2,border=True)
  # with premium:
  #   fig_premium = charts.price_distribution_premium_histogram()
  #   st.header('Premium Tier Distribution Histogram',text_alignment='center')
  #   st.plotly_chart(fig_premium,key='premium')

  # with luxury:
  #   fig_luxury = charts.price_distribution_luxury_histogram()
  #   st.header('Luxury Tier Distribution Histogram',text_alignment='center')
  #   st.plotly_chart(fig_luxury,key='luxury')

  with st.container():

    tier_count, most_expensive = st.columns(2,border=True)

    with tier_count:
      fig_tier_count = charts.price_tier_count_chart()
      st.header('Number of Products In Each Segment',text_alignment='center')
      st.plotly_chart(fig_tier_count)

    with most_expensive:
      fig_most_expensive = charts.most_expensive_chart()
      st.header('Most Expensive Products',text_alignment='center')
      st.plotly_chart(fig_most_expensive)

    bluetooth_distri,scatter_plot = st.columns(2,border=True)

    with bluetooth_distri:
      fig_bluetooth_distri = charts.bluetooth_distri_chart()
      st.header('Bluetooth Version Chart %')
      st.plotly_chart(fig_bluetooth_distri)

    with scatter_plot:
      fig_scatter_plot = charts.scatter_plot_chart()
      st.header('Price vs Rating Scatter',text_alignment='center')
      st.plotly_chart(fig_scatter_plot)


import streamlit as st
import utils.charts as charts


def show():

  budget,mid = st.columns(2,border=True)
  with budget:
    fig_budget = charts.price_distribution_budget_histogram()
    st.header('Budget Tier Distribution Histogram',text_alignment='center')
    st.plotly_chart(fig_budget,key='budget')

  with mid:
    fig_mid = charts.price_distribution_mid_histogram()
    st.header('Mid-Range Tier Distribution Histogram',text_alignment='center')
    st.plotly_chart(fig_mid,key='mid')

  premium,luxury =  st.columns(2,border=True)
  with premium:
    fig_premium = charts.price_distribution_premium_histogram()
    st.header('Premium Tier Distribution Histogram',text_alignment='center')
    st.plotly_chart(fig_premium,key='premium')

  with luxury:
    fig_luxury = charts.price_distribution_luxury_histogram()
    st.header('Luxury Tier Distribution Histogram',text_alignment='center')
    st.plotly_chart(fig_luxury,key='luxury')

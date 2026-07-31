import streamlit as st
import plotly.graph_objects as go
from database.queries import overview_query

overview_query = overview_query()


# overview page charts
def top_count_company_chart():
  company,count = overview_query.top_count_company()
  fig = go.Figure(
    go.Pie(
      labels=company,
      values = count,
      hoverinfo='label+percent',
      textinfo='value'
    )
  )
  return fig

def wired_wireless_chart():
  wireless = overview_query.wireless_percent()
  wired = overview_query.wired_percent()

  fig = go.Figure(
    go.Pie(
      labels = ['wireless','wired'],
      values = [wireless,wired],
      hole = 0.5,
      hoverinfo = 'label'
    )
  )
  return fig

def price_tier_chart():
    tier,count = overview_query.price_tier()
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
    return fig

def top_avg_price_chart():
   company,avg_price,count = overview_query.top_avg_price()
   fig = go.Figure(
     go.Bar(
       x = company,
       y = avg_price,
       text = avg_price,
       textposition = 'inside',
       customdata = count,
       hovertemplate=
                "<b>%{x}</b><br>"
                "Average Price: ₹%{y:,.0f}<br>"
                "Products: %{customdata}<extra></extra>"
     )
   )
   fig.update_layout(
     title = 'Top 15 Brands by Average Headphone Price',
     xaxis_title = 'Brand',
     yaxis_title = 'Average Price'
   )
   return fig



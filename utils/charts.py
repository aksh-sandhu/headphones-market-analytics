import streamlit as st
import plotly.graph_objects as go
from database.queries import query

query = query()

# overview page charts
def top_count_company_chart():
  company,count = query.top_count_company()
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
  return fig

def price_tier_chart():
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
    return fig

def top_avg_price_chart():
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
   return fig


# market_insights page charts
def price_distribution_budget_histogram():
   price = query.price_distribution_budget()
   fig = go.Figure(
      go.Histogram(
         x =  price,
         nbinsx = 30
      )
   )

   fig.update_layout(
      title = 'Price Distribution',
      xaxis_title = 'Price (INR)',
      yaxis_title = 'Number of products'
   )

   return fig

def price_distribution_mid_histogram():
   price = query.price_distribution_mid()
   fig = go.Figure(
      go.Histogram(
         x =  price,
         nbinsx = 30
      )
   )

   fig.update_layout(
      title = 'Price Distribution',
      xaxis_title = 'Price (INR)',
      yaxis_title = 'Number of products'
   )
   return fig

def price_distribution_premium_histogram():
      price = query.price_distribution_premium()
      fig = go.Figure(
      go.Histogram(
         x =  price,
         nbinsx = 30
      )
   )

      fig.update_layout(
      title = 'Price Distribution',
      xaxis_title = 'Price (INR)',
      yaxis_title = 'Number of products'
      )
      return fig

def price_distribution_luxury_histogram():
      price = query.price_distribution_luxury()
      fig = go.Figure(
      go.Histogram(
         x =  price,
         nbinsx = 30
      )
   )

      fig.update_layout(
      title = 'Price Distribution',
      xaxis_title = 'Price (INR)',
      yaxis_title = 'Number of products'
      )
      return fig

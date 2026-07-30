import streamlit as st
import plotly.graph_objects as go
from database.queries import market_insights_query

market_insights_query = market_insights_query()


# market_insights page charts


def price_distribution_budget_histogram():
   price = market_insights_query.price_distribution_budget()
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
   price = market_insights_query.price_distribution_mid()
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
      price = market_insights_query.price_distribution_premium()
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
      price = market_insights_query.price_distribution_luxury()
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






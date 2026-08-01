import streamlit as st
import plotly.graph_objects as go
from database.queries import market_insights_query

query = market_insights_query()


# market_insights page charts


# def price_distribution_budget_histogram():
#    price = market_insights_query.price_distribution_budget()
#    fig = go.Figure(
#       go.Histogram(
#          x =  price,
#          nbinsx = 30
#       )
#    )

#    fig.update_layout(
#       title = 'Price Distribution',
#       xaxis_title = 'Price (INR)',
#       yaxis_title = 'Number of products'
#    )

#    return fig

# def price_distribution_mid_histogram():
#    price = market_insights_query.price_distribution_mid()
#    fig = go.Figure(
#       go.Histogram(
#          x =  price,
#          nbinsx = 30
#       )
#    )

#    fig.update_layout(
#       title = 'Price Distribution',
#       xaxis_title = 'Price (INR)',
#       yaxis_title = 'Number of products'
#    )
#    return fig

# def price_distribution_premium_histogram():
#       price = market_insights_query.price_distribution_premium()
#       fig = go.Figure(
#       go.Histogram(
#          x =  price,
#          nbinsx = 30
#       )
#    )

#       fig.update_layout(
#       title = 'Price Distribution',
#       xaxis_title = 'Price (INR)',
#       yaxis_title = 'Number of products'
#       )
#       return fig

# def price_distribution_luxury_histogram():
#       price = market_insights_query.price_distribution_luxury()
#       fig = go.Figure(
#       go.Histogram(
#          x =  price,
#          nbinsx = 30
#       )
#    )

#       fig.update_layout(
#       title = 'Price Distribution',
#       xaxis_title = 'Price (INR)',
#       yaxis_title = 'Number of products'
#       )
#       return fig

def price_tier_count_chart():

  budget,luxury,mid_range,premium = query.price_tier_count_query()
  counts = [budget,mid_range,luxury,premium]
  fig = go.Figure(
    go.Bar(
      x = ['budget','mid_range','luxury','premium'],
      y = [budget,mid_range,luxury,premium],
      text = counts,
      textposition = 'inside'
    )
  )

  fig.update_layout(
    title = 'Brand Segment Counts',
    xaxis_title = ' Price Segments',
    yaxis_title = 'Number of Products'
  )

  return fig

def most_expensive_chart():

  info,price = query.most_expensive_query()

  fig = go.Figure(
    go.Bar(
      x = info,
      y = price,
      text = price,
      textposition = 'inside'
    )
  )

  fig.update_layout(
    title = 'Top 10 Most Expensive Products',
    xaxis_title = 'Company and Model',
    yaxis_title = 'Price (INR)'
  )

  return fig


def bluetooth_distri_chart():

  bluetooth,count = query.bluetooth_distri_query()

  fig = go.Figure(
    go.Pie(
      labels = bluetooth,
      values = count,
      hole = 0.45,
      textinfo = 'label+percent',
      hovertemplate='<b>%{label}</b><br>Products: %{value}<br>Share: %{percent}<extra></extra>'
    )
  )

  fig.update_layout(
    title='Bluetooth Version Distribution',
    legend=dict(
        title=dict(
            text='Bluetooth Versions'
        )
    )
)

  return fig

def scatter_plot_chart():

  price,rating = query.scatter_plot_query()

  fig = go.Figure(
    go.Scatter(
      x = price,
      y = rating,
      mode='markers',
            marker=dict(
                size=5,
                opacity=0.5
            ),
            hovertemplate=
    "<b>%{text}</b><br>" +
    "Price: ₹%{x}<br>" +
    "Rating: %{y}<extra></extra>"

    )
  )

  fig.update_layout(
    title = 'Price vs Rating',
    xaxis_title = 'Price INR (Log scale)',
    yaxis_title = 'Rating'
  )

  fig.update_xaxes(
    type = 'log'
  )

  return fig







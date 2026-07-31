import streamlit as st
import plotly.graph_objects as go
from database.queries import brand_analysis_query

query = brand_analysis_query()


def top_company_count_chart():
  company,count = query.top_products()

  fig = go.Figure(
    go.Bar(
      x = company,
      y = count,
      text = count,
      textposition = 'inside'
    )
  )

  fig.update_layout(
    title = 'Top Companies With Most Products',
    xaxis_title = 'Companies',
    yaxis_title = 'Number of Products'
  )

  return fig

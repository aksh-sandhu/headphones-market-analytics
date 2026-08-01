import streamlit as st
import plotly.graph_objects as go
import sidebar.overview as overview
import sidebar.about_dataset as about_dataset
import sidebar.market_insights as market_insights
import sidebar.brand_analysis as brand_analysis

st.set_page_config(
  page_title="Headphones Market Analytics",
  layout = 'wide'
)



user_option = st.sidebar.selectbox('Choose',['Overview','Market Insights','Brand Analysis',"About Dataset"])

if user_option == 'Overview':
  overview.show()

elif user_option == 'Market Insights':
  market_insights.show()

elif user_option == 'Brand Analysis':
  brand_analysis.show()

elif user_option == 'About Dataset':
  about_dataset.show()


st.sidebar.divider()

st.sidebar.markdown("### 👨‍💻 Developer")

st.sidebar.link_button(
    "🔗 LinkedIn",
    "https://www.linkedin.com/in/akshdeep-singh-sandhu-1377aa230/"
)

st.sidebar.link_button(
    "🐙 GitHub",
    "https://github.com/aksh-sandhu"
)

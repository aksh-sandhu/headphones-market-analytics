import os
import streamlit as st

try:
    HOST = st.secrets["HOST"]
    USER = st.secrets["USER"]
    PASSWORD = st.secrets["PASSWORD"]
    DATABASE = st.secrets["DATABASE"]
except Exception:
    HOST = os.getenv("HOST")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    DATABASE = os.getenv("DATABASE")

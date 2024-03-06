# Import Streamlit
import streamlit as st

st.write("Test")
with st.sidebar:
  st.radio("MENU",["Home","Contact","Projects"])

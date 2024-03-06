# Import Streamlit
import streamlit as st

st.write("Test")
with st.sidebar:
  x = st.radio("MENU",["Home","Contact","Projects"])
if x=="Home":
  st.write("Page Home")
if x=="Contact":
  st.write("Page Contact")
if x=="Projects":
  st.write("Page Projects")


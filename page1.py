# Import Streamlit
import streamlit as st
import streamlit.components.v1 as components


st.write("Test")
html_string = "<h3>this is an html string</h3>"
st.markdown(html_string, unsafe_allow_html=True)
with st.sidebar:
  x = st.radio("MENU",["Home","Contact","Projects"])
if x=="Home":
  st.write("Page Home")

if x=="Contact":
  st.write("Page Contact")
if x=="Projects":
  st.write("Page Projects")


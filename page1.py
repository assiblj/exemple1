# Import Streamlit
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Multipage App",
    page_icon="📑",
)
st.image("patcha.jpg")


# Main Page
st.title("Main Page")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered:", my_input)

# Projects Page
st.title("Projects")
st.write("You have entered:", st.session_state["my_input"])

# Contact Page
st.title("Contact")

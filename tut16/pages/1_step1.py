import streamlit as st

st.set_page_config(page_icon="✈️", page_title="FancyApp", layout="wide")

st.title("step1")
input_name = st.text_input("Name:")
st.write(input_name)


# you have to use session_state to store information...
# st.switch_page()
# st.navigation()


import streamlit as st
import os


# sidebar
st.sidebar.title("This is sidebar")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


# tabs
tab1, tab2, tab3 = st.tabs(["tab1", "tab2", "tab3"])

with tab1:
    "this is tab1"
with tab2:
    "this is tab2"
with tab3:
    "this is tab3"



# columns
# col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns((10, 1, 1))

with col1:
    st.write("this is col1")

with col2:
    st.write("this is col2")

with col3:
    st.write("this is col3")


# container (just a box)
with st.container(border=True):
    st.write("stuff whthin as container...")
    st.write("stuff whthin as container...")
    st.write("stuff whthin as container...")
    st.write("stuff whthin as container...")
    st.write("stuff whthin as container...")


# placeholder
placeholder = st.empty()
if st.button("fill empty data"):
    # placeholder.write("This is generated from an empty folder.")
    # placeholder.warning("here is a warning")
    # placeholder.error("here is an error")
    pass


# Expander
with st.expander("Expand for details"):
    st.image(os.path.join(os.getcwd(), 'static', "ny_skyline.jpg"))


# tooltip
st.button("refresh", help="click me to refresh button...")



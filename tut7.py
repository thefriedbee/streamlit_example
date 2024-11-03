import streamlit as st

# understand the rerun logic, flow control...

# date time form
st.date_input(label="birthday", value='today')

start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("red", "blue"),
)

st.write(f"selected color range from {start_color} to {end_color}")



with st.form(key="input"):
    start_color, end_color = st.select_slider(
        "Select a range of color wavelength",
        options=[
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "indigo",
            "violet",
        ],
        value=("red", "blue"),
    )

    st.write(f"selected color range from {start_color} to {end_color}")

    but_submitted = st.form_submit_button()



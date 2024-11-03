"""
widgets
"""

import streamlit as st

# example 1 (fix it)
# input_b1 = st.button("ok")
# input_b2 = st.button("ok")


# example 1 (fixed)
# input_b1 = st.button("ok")
# input_b2 = st.button("ok", key="b2")


# example 2 (fix it)
# min_age = st.slider("set min age:", 0, 18)
# age_range = st.slider("age range:", min_age, 100, min_age)


# example 2 (fixed)
# if 'current_age' not in st.session_state:
#     st.session_state.current_age = 100

# min_age = st.slider("set min age:", 0, 18)
# age_range = st.slider(
#     "age range:", min_age, 100,
#     st.session_state.current_age
# )

# st.session_state.current_age = age_range


# example 3 (fix: loss information)
# if st.checkbox("Show name input"):
#     input_name = st.text_input("Name")
#     st.write(f"You name is {input_name}")


# example 3 (fixed)
if 'name' not in st.session_state:
    st.session_state["name"] = ""


if st.checkbox("Show name input"):
    input_name = st.text_input("Name", value=st.session_state["name"])
    st.write(f"You name is {input_name}")
    st.session_state["name"] = input_name






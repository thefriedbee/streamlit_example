import streamlit as st


if "count" not in st.session_state:
    st.session_state["count"] = 0

st.write(f"current val: {st.session_state.count}")

def increment_and_rerun():
    st.session_state.count += 1
    # st.rerun()

if st.button("click one"):
    increment_and_rerun()


# method 1: change order of code
# method 2: use st.empty()
# method 3: use st.rerun()

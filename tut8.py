import streamlit as st

# # build a counter
# # wrong example
# num_clicked = 0

# if st.button(label="Increment 1"):
#     num_clicked += 1

# print(num_clicked)
# st.write(num_clicked)




# fix
if 'clicked' not in st.session_state:
    num_clicked = 0
else:
    num_clicked = st.session_state["clicked"]


if st.button(label="Increment 1"):
    num_clicked += 1
    st.session_state["clicked"] = num_clicked

print(num_clicked)
st.write(num_clicked)
# try to click refresh button...


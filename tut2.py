import streamlit as st

print("start run")
pressed1 = st.button("button 1")
print("pressed1:", pressed1)

pressed2 = st.button("button 2")
print("pressed2:", pressed2)

# each component has its unique id
# pressed2 = st.button("button 2", key="b2")
# print("pressed2:", pressed2)

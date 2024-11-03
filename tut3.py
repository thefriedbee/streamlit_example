import streamlit as st
import os

st.title("Title here")
st.header("here is a header")
st.subheader("here is a subheader")

st.markdown("# Markdown title")
st.markdown("This is _Markdown_")
st.caption("this is caption")

code_example = """
print("Hello World")
lst = [i for i in range(10)]
for item in lst:
    print(item)
"""
st.code(code_example, language="python")

st.divider()

st.image(os.path.join(os.getcwd(), "static", "ny_skyline.jpg"))



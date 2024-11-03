"""
Use framgments to run only a part of the program...
"""
import streamlit as st
import datetime
import numpy as np
import pandas as pd


@st.fragment()
def part1():
    st.write("part1")
    st.write(datetime.datetime.now())
    st.button("update time")
    # st.rerun(scope="app")
    # st.rerun(scope="fragment")
    # cannot return data in the end of fragment function (make sense)
    # use session state to return value
    pass



@st.fragment()
def part2():
    x = np.random.random(50)
    y = np.random.random(50)
    df = pd.DataFrame({
        "x": x,
        "y": y
    })
    print(df.head())
    st.write("part2")
    st.scatter_chart(data=df, x="x", y="y")

part1()
part2()




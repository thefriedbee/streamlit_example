import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Bob", "Lex", "David"],
    "age": [24, 32, 46],
    "salary": [7000, 5000, 6000],
    "home_lat": [37.76, 37.50, 37.59],
    "home_lon": [-122.4, -122.36, -122.42],
})


st.subheader("Altair plot")
st.line_chart(data=df, x="age", y="salary")
st.scatter_chart(data=df, x="age", y="salary")
st.bar_chart(data=df, x="name", y="salary")


chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns=["a", "b", "c"]
)
st.area_chart(chart_data)

# altair
x = np.arange(100)
source = pd.DataFrame({ 
  'x': x,
  'f(x)': np.sin(x / 5)
})
alt_plot = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
)
st.altair_chart(alt_plot)


# matplotlib
st.subheader("Matplotlib")
fig, ax = plt.subplots()
ax.plot(df.age, df.salary, 'b+')
ax.set_xlabel("age")
ax.set_ylabel("salary")
ax.set_ylim(bottom=0)
st.pyplot(fig)
# fig


st.subheader("Map")
st.map(df, latitude="home_lat", longitude="home_lon")












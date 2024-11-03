import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Name": ["Bob", "Lex", "David"],
    "age": [24, 32, 46],
    "salary": [7000, 5000, 6000]
})

st.dataframe(df)
edited_df = st.data_editor(df)
print(edited_df)

st.table(edited_df)


st.metric(label="total number of rows:", value=len(edited_df))
st.metric(label="average year:", value=edited_df.age.mean())

st.json(edited_df.to_json())



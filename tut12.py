import streamlit as st
import time
import pandas as pd

# example 1
# @st.cache_data(ttl=2)
# def fetch_data():
#     time.sleep(3)
#     return {f"APPL": "$230"}

# t0 = time.perf_counter()
# st.json(fetch_data())
# t1 = time.perf_counter()

# st.write(f"It takes {t1 - t0:.2f} seconds to run the code")





# example 2 (function with parameter)
@st.cache_data
def fetch_data(stock_name="APPL"):
    time.sleep(3)
    return {f"{stock_name}": "$230"}

t0 = time.perf_counter()
stock_abbr = st.text_input("enter stock name:")
if stock_abbr:
    st.json(fetch_data(stock_abbr))

    t1 = time.perf_counter()
    st.write(f"It takes {t1 - t0:.2f} seconds to run the code")



# notice:
# 1. @st.cache_data(ttl=60)
# 2. need to make sure the returned item is fixed
# 3. returned must be hashable

# @st.cache_data
# def fetch_data():
#     time.sleep(3)
#     df = pd.DataFrame({
#         "Name": ["Bob", "Lex", "David"],
#         "age": [24, 32, 46],
#         "salary": [7000, 5000, 6000]
#     })
#     return [1, 2, 3]

# t0 = time.perf_counter()
# st.dataframe(fetch_data())
# t1 = time.perf_counter()

# st.write(f"It takes {t1 - t0:.2f} seconds to run the code")



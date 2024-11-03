import streamlit as st
import datetime

file_pth = "example.txt"

# this is actually bad to be honest...
# to me, streamlit is a dashboard (not for data modification)
# @st.cache_resource
def get_file_info():
    file = open(file_pth, "a+")
    return file

file_handler = get_file_info()


if st.button("Write to File"):
    ts = datetime.datetime.now()
    file_handler.write(f"New rec: {ts}\n")
    # ensure information is updated immediately
    file_handler.flush()
    st.success(f"wrote a new information: New rec: {ts}")

if st.button("Read File"):
    # move cursor to the beginning of the file
    file_handler.seek(0)
    content = file_handler.readlines()
    st.write(content)

# if st.button("close connection"):
#     file_handler.close()
#     st.success(f"closed connection.")

st.button("close connection", on_click=file_handler.close)








# AI better example by Claude
# import streamlit as st
# import sqlite3
# from sqlalchemy import create_engine
# import pandas as pd
# from contextlib import contextmanager
# from typing import Generator
# import threading

# # BAD PATTERN: Single cached connection
# @st.cache_resource
# def get_single_connection():
#     """
#     This pattern is problematic because:
#     1. The same connection is shared between users
#     2. SQLite doesn't handle concurrent access well
#     3. Can lead to "database is locked" errors
#     """
#     return sqlite3.connect("database.db", check_same_thread=False)

# # BETTER PATTERN: Connection Pool
# @st.cache_resource
# def get_connection_pool():
#     """
#     Create a connection pool that can be safely shared between users.
#     Each user gets their own connection from the pool.
#     """
#     return create_engine(
#         "sqlite:///database.db",
#         pool_size=20,  # Maximum number of connections in the pool
#         max_overflow=0,  # Maximum number of connections that can be created beyond pool_size
#         pool_timeout=30,  # Seconds to wait before giving up on getting a connection
#         pool_recycle=1800,  # Recycle connections after 30 minutes
#     )

# # BEST PATTERN: Context manager for safe connection handling
# @contextmanager
# def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
#     """
#     Safely manage database connections with proper cleanup.
#     Usage:
#         with get_db_connection() as conn:
#             df = pd.read_sql("SELECT * FROM table", conn)
#     """
#     pool = get_connection_pool()
#     connection = pool.connect()
#     try:
#         yield connection
#     finally:
#         connection.close()

# # Example Streamlit app demonstrating safe concurrent access
# def main():
#     st.title("Safe Database Access Demo")
    
#     # Simulate concurrent user actions
#     if st.button("Perform Database Operation"):
#         with get_db_connection() as conn:
#             # Each user gets their own connection from the pool
#             query = "SELECT * FROM your_table WHERE user_id = ?"
#             df = pd.read_sql(query, conn, params=[st.session_state.get("user_id")])
#             st.write(df)

#     # Example of how to handle transactions safely
#     def safe_transaction():
#         with get_db_connection() as conn:
#             try:
#                 # Start transaction
#                 trans = conn.begin()
#                 # Perform operations
#                 conn.execute("UPDATE table SET value = ? WHERE id = ?", 
#                            [new_value, id])
#                 # Commit if successful
#                 trans.commit()
#             except Exception as e:
#                 # Rollback on error
#                 trans.rollback()
#                 raise e

# if __name__ == "__main__":
#     main()
import streamlit as st


# wrong example
# if "step" not in st.session_state:
#     st.session_state["step"] = 1


# if st.session_state.step == 1:
#     st.write("This is step 1 info")
#     # if st.button(label="Go to next step"):
#     #     st.session_state["step"] = 2
#     but_clicked = st.button(label="Go to next step")
#     if but_clicked:
#         st.session_state["step"] = 2


# if st.session_state.step == 2:
#     st.write("This is step 2 info")
#     if st.button(label="Go to prev step"):
#         st.session_state["step"] = 1



# correct version
if "step" not in st.session_state:
    st.session_state["step"] = 1


def goto_step(step_num: int):
    st.session_state["step"] = step_num
    # st.write(text)


if st.session_state.step == 1:
    st.title("Step 1 page")
    st.button(label="Go to next step", on_click=goto_step, args=(2,))


if st.session_state.step == 2:
    st.title("Step 2 page")
    st.button(label="Go to prev step", on_click=goto_step, args=(1,))












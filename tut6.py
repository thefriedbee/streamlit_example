import streamlit as st


with st.form(key="form1"):
    respond_info = {
        "name": None,
        "team": None,
        "share_info": None,
        "email_info": None,
        "age_info": None
    }

    respond_info["name"] = st.text_input(label="Name")
    respond_info["team"] = st.selectbox(
        label="favorate team:",
        options=["Arsenal", "Man City", "Man United", "Chelsea", "Liverpool"]
    )
    respond_info["share_info"] = st.radio(label="share my information:", options=["yes", "no"])
    respond_info["email_info"] = st.checkbox(label="Receive Email notification")
    respond_info["age_info"] = st.slider(label="age", min_value=0, max_value=100)
    # submit button
    form_submitted = st.form_submit_button(label="Submit!")

    def check_form_valid():
        vals = respond_info.values()
        return all([True if val not in [None, ""] else False for val in vals ])

    # check format
    if form_submitted:
        if not check_form_valid():
            st.warning("Please fill in all form values!")
        else:
            # st.balloons()
            st.write("form submitted!")


print(respond_info)
respond_info


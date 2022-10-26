import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from database import *
from urllib.error import URLError

st.set_page_config(page_title="Register")
st.header("Registration")

try:
    username = st.text_input("User Name")
    email = st.text_input("Email")
    password = st.text_input("Password")
    hashing_password = make_hashes(password)
    if st.button("Register"):
        result = fetch_email(email)
        if (result!=None):
            st.warning("User Already exists, Please click on Login button")
        else:
            add_user(username,email,hashing_password)
            st.success("Account registration successfull")
            st.info("Go to login menu for login")

except URLError as e:
    st.error(
        """
        **This page requires internet access.**
        Connection error: %s
    """
        % e.reason
    )


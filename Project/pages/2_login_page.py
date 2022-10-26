import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from database import *
from urllib.error import URLError
import time
#from Resume_screening_page import file_uploader
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import get_pages
#from file_uploader_result import *

if "authenticated" not in st.session_state:
    st.session_state['authenticated'] = False

st.set_page_config(page_title="Login")
st.header("Login")

try:
    st.subheader("Login")
    username = st.text_input("Email")
    st.session_state['username'] = username
    password = st.text_input("Password")
    if st.button("Login"):
        if (username == '') and (password == ''):
            st.warning("Please provide email and password")
        if (username == '') and (password != ''):
            st.warning("Please provide email")
        if (username != '') and (password== ''):
            st.warning("Please provide password")
        
        if (username != '') and (password != ''):
            hashed_password = make_hashes(password)
            result = email_login_check(username,check_hashes(password,hashed_password))
            if result:
                st.success("Logged In as {}".format(username))
                st.write("You are successfully logged in Now go to file uploader")
                #st.button("Login")
                st.session_state['authenticated'] = True
                #edit = st.button(label = "File Uploader")
                    
                    # get_pages("file_uploader_result.py")
                    # st.session_state.runpage = file_uploader_result.file_uploader()
                    # st.session_state.runpage()
                    # st.experimental_rerun()

            else:
                st.warning("Incorrect username/password")

    



except URLError as e:
    st.error(
        """
        **This page requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
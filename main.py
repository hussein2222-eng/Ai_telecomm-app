import streamlit as st

from login import login
from AI_TELECOM import home

# Create session variable first time only
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "full_name" not in st.session_state:
    st.session_state.full_name = ""
    
# Routing
if st.session_state.logged_in:
    home(st.session_state.full_name)
else:
    name = login()
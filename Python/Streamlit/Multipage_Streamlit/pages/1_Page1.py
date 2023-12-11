import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Page 1", page_icon=None)

st.markdown("# Page 1")
st.sidebar.header("Page 1 Sidebar")
st.markdown(
    """Page 1 description"""
)


inputs1 = st.text_input("Enter text 1:", '')
inputs2 = st.text_input("Enter text 2:", '')
inputs3 = st.text_input("Enter text 3:", '')

if inputs1 and inputs2 and inputs3:
  st.write = 'completed form'
  inputs1, inputs2, inputs3 = '','',''
  switch_page("page2")

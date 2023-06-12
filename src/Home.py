import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="👽", page_title="Chat-Bot 🤖")


#Contact
with st.sidebar.expander("👨‍💻Contact"):
        
    st.write("**Mail** : subhajit8903@gmail.com")
    st.write("**Created by Subhajit Mondal**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Your data-aware assistant </h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Chatbot, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive natural language interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV 😊</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.markdown(
    """
    <h2 style='text-align: center;'>Your PwCbot👽</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")









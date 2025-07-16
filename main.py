import streamlit as st
import pandas as pd 

# Input fields
name = st.text_input("Enter your name : ")
fathername = st.text_input("Enter your father name : ")
adr = st.text_area("Enter your Text : ")
classdata = st.selectbox("Enter your Class : ", (1, 2, 3, 4, 5, 6))

# Button and Output
button = st.button("Done")
if button:
    st.markdown(f"""
    **Name:** {name}  
    **Father Name:** {fathername}  
    **Address:** {adr}  
    **Class:** {classdata}
    """)

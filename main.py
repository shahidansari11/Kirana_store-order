import streamlit as st

st.header("KGN KIRANA STORE : ")

st.subheader("Ph No : 9145206349: ")
st.markdown("Home delivery free:")

import streamlit as st

name=st.text_input("Enter your name : ") 

order=st.text_area("Enter your order :")

address=st.text_area("Enter your full Address : ")

classdata= st.text_input("Enter your phone number : ")

button=st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}
    ,Order : {order}
    ,Address : {address}
    ,Ph No : {classdata}""")
st.markdown("Thank you for visit us : ")


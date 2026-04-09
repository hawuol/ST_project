import streamlit as st

st.title("카운터 앱")
count = 0
if st.button("증가"):
    count = count+1
st.write("현재 숫자: `{count}`")

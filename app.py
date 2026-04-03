import streamlit as st

st.title("앱 UI 만들기")
name = st.text_input("이름")
grade = st.selectbox("학년", [1,2,3])
cls = st.number_input("반")
level = st.radio("난이도", ["쉬움", "보통", "어려움"])
score = st.slider("점수", 0, 100)


if st.button("확인"):
    st.success(f"{name} / {grade}학년 / {cls}반 / {level}")
    st.markdown(f"점수: `{score}`")

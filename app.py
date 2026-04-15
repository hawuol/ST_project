import streamlit as st

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'user_goal' not in st.session_state:
    st.session_state.user_motto = "오늘도 화이팅!"

st.title("🌱 완벽한 하루 플래너")

st.header("📣 1. 오늘의 다짐")
motto = st.text_input("나의 한 줄 좌우명을 적어주세요")
if st.button("다짐 저장"):
    st.session_state.user_motto = motto
    st.success("좌우명이 등록되었습니다!")
st.markdown("---")

st.header("✅ 2. 오늘의 할 일")
st.write(f"현재 다짐: **{st.session_state.user_motto}**")
new_todo = st.text_input("추가할 할 일을 입력하세요")
if st.button("추가하기"):
    if new_todo:
        st.session_state.todo_list.append({"task": new_todo, "done": False})
        st.toast("할 일이 추가되었습니다!")
st.markdown("---")
for i, item in enumerate(st.session_state.todo_list):
    col_task, col_check = st.columns([4, 1])
    with col_task:
        st.write(f"{i+1}. {item['task']}")
    with col_check:
        if st.button("완료", key=f"btn_{i}"):
            item['done'] = True
            st.success("달성!")
st.markdown("---")

st.header("📈 3. 나의 갓생 지수")
if not st.session_state.todo_list:
    st.write("아직 등록된 할 일이 없습니다.")
else:
    total = len(st.session_state.todo_list)
    done_count = sum(1 for item in st.session_state.todo_list if item['done'])
    progress = (done_count / total) * 100
    
    st.metric("오늘의 달성률", f"{progress:.1f}%")
    st.progress(progress / 100)
    
    if st.button("기록 전체 초기화"):
        st.session_state.todo_list = []
        st.rerun()

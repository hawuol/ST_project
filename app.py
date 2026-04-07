import streamlit as st

# 1. [sidebar] 사이드바: 앱 전체 설정 및 제어
with st.sidebar:
    st.header("⚙️ 앱 설정")
    user_name = st.text_input("사용자 이름", value="게스트")
    app_mode = st.radio("작업 모드", ["편집 모드", "보기 모드"])
    st.divider()
    st.info(f"접속자: {user_name}")

# 메인 타이틀
st.title("📊 데이터 관리 대시보드")
st.write(f"{user_name}님, 환영합니다! 오늘 수행할 작업을 선택하세요.")

# 2. [tabs] 탭: 큰 카테고리 분류
tab1, tab2 = st.tabs(["📁 데이터 입력", "📈 통계 확인"])

with tab1:
    st.subheader("새 데이터 등록")
    
    # 3. [columns] 컬럼: 위젯 가로 배치 (1:1 비율)
    col1, col2 = st.columns(2)
    
    with col1:
        item_name = st.text_input("품목명", placeholder="예: 노트북")
        item_price = st.number_input("단가", min_value=0, step=1000)
    
    with col2:
        item_cat = st.selectbox("카테고리", ["전자제품", "도서", "식품"])
        item_count = st.number_input("수량", min_value=1, value=1)

    # 4. [container] 컨테이너: 실행 결과 묶어서 강조하기
    if st.button("등록하기"):
        with st.container(border=True): # 테두리가 있는 박스로 묶기
            st.write("### ✅ 등록 확인")
            st.write(f"**품목:** {item_name} ({item_cat})")
            st.write(f"**총 금액:** {item_price * item_count}원")
            st.success("데이터베이스에 성공적으로 저장되었습니다.")

with tab2:
    st.subheader("전체 요약 통계")
    # 컬럼을 3개로 나누어 수치만 강조
    stat1, stat2, stat3 = st.columns(3)
    stat1.metric("오늘 방문자", "120명", "12%")
    stat2.metric("신규 등록", "15건", "5%")
    stat3.metric("성공률", "98%", "1%")

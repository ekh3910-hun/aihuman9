#app.py
#python -m streamlit run ./webservice/day31/myapp/app.py
#streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
import os
import streamlit as st
from dotenv import load_dotenv
from streamlit.source_util import page_icon_and_name
load_dotenv()

DEFAULT_GREETING = "안녕하세요"
APP_GREETING = os.getenv("APP_GREETING", DEFAULT_GREETING)

st.set_page_config(page_title='Render배포 연습앱',
                   page_icon = '🚀',
                   layout='centered',)

st.title('🚀Render배포 연습앱')
st.write('APP_GREETING')

st.divider()

st.subheader('간단한 인사말')

name = st.text_input('이름입력',placeholder= '예) 홍길동')

if st.button('인사말 확인',type='primary'):
    if name.strip():
        st.success(f'{APP_GREETING},{name.strip()}님 배포잘되었습니다')
    else:
        st.warning('이름입력')

st.divider()

st.subheader('환경변수설정')

if os.getenv('APP_GREETING'):
    st.success('APP_GREETING 환경변수 읽음')
    st.write(f'인사말: {APP_GREETING}')
else:
    st.info(f'APP_GREETING 환경변수가 설정 안됨')

























































import streamlit as st
import datetime

st.title("宿題ペース計算")

i_d = datetime.date.today()

f_d = st.date_input(
    "完成目標日：",
    i_d
)

page_num = st.number_input('残りページ数を入力してください：')
s_d = f_d - i_d

try:
    task_day = page_num / (4*(s_d.days / 7))
    task_day_6 = page_num / (6*(s_d.days / 7))
    task_week = page_num / (s_d.days / 7)
    st.metric(label="4日2日ペース：", value=f'{int(task_day)}ページ/日')
    st.metric(label="6日ペース：", value=f'{int(task_day_6)}ページ/日')
    st.metric(label="1週間：", value=f'{int(task_week)}ページ/週')
except ZeroDivisionError:
    st.write("")
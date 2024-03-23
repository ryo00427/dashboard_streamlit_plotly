import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('streamlit 超入門')

st.write('dateframe')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
'done'




#text = st.text_input('あなたの趣味を教えてください。')
#condition = st.slider('あなたの今の調子は？',0,100,50)
#'あなたの趣味は:',text
#'コンディション:',condition


#expander1 = st.expander('問い合わせ')
#expander1.write('問い合わせ１の内容を書く')

#left_column, right_column = st.columns(2)
#button = left_column.button('右カラムに文字を表示')
#if button:
#    right_column.write('ここは右カラム')

import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st
st.title('株価可視化アプリ')

st.sidebar.slider('''
#GAFA株価
こちら株価可視化ツールです。以下のオプションを選んでください
''')

st.sidebar.write('''
#表示日数選択
''')
    
days = st.sidebar.slider('日数',1,50,20)

st.write(f'''
### 過去 **{days}日刊**のGAFA株価
''')
@st.cache_data
def get_data(days,tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        #yfinanceからデータを参照する
        hist = tkr.history(period=f'{days}d')
        #選択した日数まで表示する
        hist.index = hist.index.strftime('%d %B %Y')
        #日付　
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

st.sidebar.slider('''
## 株価の範囲指定
''')



ymin, ymax = st.sidebar.slider(
    '範囲を指定してください',
    0.0,3500.0,(0.0,3500.0)
) 

tickers = {
    'apple':'AAPL',
    'facebook':'META',
    'google':'GOOGL',
    'microsoft':'MSFT',
    'netflix':'NFLX',
    'amazon':'AMZN'
}
df = get_data(days, tickers)
companies = st.multiselect(
    '会社名を選択してください',
    list(df.index),
    ['google','amazon','facebook','apple']
)

if not companies:
     st.error('少なくとも一社は選んでください。')
else:
    data = df.loc[companies]
    st.write('### 株価(USD)',data.sort_index())
    data = data.T.reset_index()
    data = pd.melt(data, id_vars = ['Date']).rename(
        columns = {'value': 'Stock Prices(USD)'}
    )

    chart = (
        alt.Chart(data)
        .mark_line(opacity =0.8, clip = True )
        .encode(
            x = 'Date:T',
            y = alt.Y('Stock Prices(USD):Q', stack = None, scale = alt.Scale(domain = [ymin,ymax])),
            color = 'Name:N'
        )
)

st.altair_chart(chart, use_container_width = True )



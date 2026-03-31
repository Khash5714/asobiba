import streamlit as st
import numpy as np
import pandas as pd

st.title("初めてのStreamlit")  #タイトルの追加

st.write("DataFrame")  #本文の追加

df=pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

st.write(df)  #表の書き方①
st.dataframe(df) #表の書き方②


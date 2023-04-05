import streamlit as st
import gspread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests, json

st.set_page_config(page_title="Just messing around",
                    page_icon=":bar_chart:",
                    layout="wide")

st.title("Welcome to StreamLit")

report_line = ['And a 1', 'And a 2', 'Time', 'And a 3']

gc = gspread.service_account("secure.json")

sh = gc.open("WeddingApp")

# ws2 = sh.add_worksheet(title="System", rows=10, cols=5)

ws = sh.worksheet("System")

st.write(ws.get('B4'))

st.write(ws.acell("B4").value)

st.write(sh.worksheets())

df = pd.DataFrame(ws.get_all_records())

ele = st.bar_chart(df,x="Country", y="2021")
st.dataframe(df)


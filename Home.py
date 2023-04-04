import streamlit as st
import gspread
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests, json

st.title("Welcome to StreamLit")

report_line = ['And a 1', 'And a 2', 'Time', 'And a 3']

gc = gspread.service_account("secure.json")

sh = gc.open("WeddingApp")

# ws2 = sh.add_worksheet(title="System", rows=10, cols=5)

ws = sh.worksheet("System")

st.write(ws.get('B4'))

st.write(ws.acell("B4").value)

st.write(sh.worksheets())

st.write(ws.row_values(3)[0])

df = pd.DataFrame(ws.get_all_records())

ele = st.line_chart(df,x="Country", y="2021")
st.dataframe(df)


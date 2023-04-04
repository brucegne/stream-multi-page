import streamlit as st
from st_aggrid import AgGrid
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

ws = sh.worksheet("Attractions")

# ws.update("B4", "Wedding")

try:
    cell = ws.find("KEY101")
    if cell:
        st.write(cell.row, cell.col)
        st.write("Found something at R%sC%s" % (cell.row, cell.col))
    else:
        st.write("Doesn't exist")
except:
    st.write("Key value not found")
    
st.write(ws.get('B4'))

st.write(ws.acell("B4").value)

# ws.update("B4", "Bingo !!!")

st.write(sh.worksheets())

st.write(ws.row_values(3)[0])

# print(sh.sheet1.row_values(4))

df = pd.DataFrame(ws.get_all_records())

# AgGrid(df)
ele = st.line_chart(df)
st.dataframe(df, use_container_width=True)

# st.dataframe(df, use_container_width=True)
# st.write(df)

response = requests.get("https://hfpintranet.appspot.com/dailyjson")
recs = response.json()
results = recs['records']

df2 = pd.DataFrame(results)
# df3 = df32.sort_values(by=['commodity','buyer','location'])[['buyer','location','commodity','basis']]

df4 = df2.groupby('commodity').mean()
ele = st.line_chart(df4)

AgGrid(df4)

for i in range(25):
    rec = results[i]
    st.write(i, '---', rec['buyer'],'---' ,rec['location'], '---', rec['basis'])
#    st.write(results[i])
                   
res = ws.get_all_records()

for rec in res:
    st.write(rec['Name'])
    
# ws.append_row(report_line)

array = np.array([[1, 2, 3], [4, 5, 6]])

# Write the array to worksheet starting from the A2 cell
# ws.update('A12', array.tolist())
# st.write(ws.get_all_values())

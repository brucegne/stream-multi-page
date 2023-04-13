import streamlit as st
import gspread
import pandas as pd
import numpy as np

report_line = ['And a 1', 'And a 2', 'Time', 'And a 3']

gc = gspread.service_account("secure.json")

sh = gc.open("WorkDataBook")

# ws2 = sh.add_worksheet(title="System", rows=10, cols=5)

ws = sh.worksheet("Attractions")
ws = sh.worksheet("titanic")

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

st.text(sh.worksheets())

st.text(ws.row_values(3)[0])

# print(sh.sheet1.row_values(4))

# df = pd.DataFrame(ws.get_all_records())

res = ws.get_all_records()

df = pd.DataFrame(ws.get_all_records())
df = df.groupby(['Age','Survived', 'Pclass'], as_index = False).agg(Score = ('Age', 'min'))
st.write(df)

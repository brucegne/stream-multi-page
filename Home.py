import streamlit as st
import gspread
import pandas as pd
import numpy as np

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
st.write(df)

res = ws.get_all_records()

for rec in res:
    st.write(rec['Name'])
    
# ws.append_row(report_line)

array = np.array([[1, 2, 3], [4, 5, 6]])

# Write the array to worksheet starting from the A2 cell
# ws.update('A12', array.tolist())
st.write(ws.get_all_values())
import gspread
import pandas as pd
import numpy as np
import pprint

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
        print(cell.row, cell.col)
        print("Found something at R%sC%s" % (cell.row, cell.col))
    else:
        print("Doesn't exist")
except:
    print("Key value not found")
    
print(ws.get('B4'))

print(ws.acell("B4").value)

# ws.update("B4", "Bingo !!!")

# print(sh.worksheets())

print(ws.row_values(3)[0])

# print(sh.sheet1.row_values(4))

# df = pd.DataFrame(ws.get_all_records())

# pprint.pprint(df)

res = ws.get_all_records()

df = pd.DataFrame(ws.get_all_records())
df = df.groupby(['Age','Survived', 'Pclass'], as_index = False).agg(Score = ('Age', 'min'))
print(df)

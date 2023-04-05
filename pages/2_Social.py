import streamlit as st
import time, json, requests

""" 
# :camera:  :boat:  :wastebasket:
"""

work_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users.json'

results = requests.get(work_url)
res = results.json()
for rec in res:
    st.write(res[rec]['name'],res[rec]['comments'])
    
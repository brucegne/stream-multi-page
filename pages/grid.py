import streamlit as st
import requests
import pandas as pd

work_url = 'https://socialpancakes-d1dad.firebaseio.com/Users.json'

# res = request.get(work_url).json()

df = pd.read_json(work_url)
df
st.write(st.dataframe(df))

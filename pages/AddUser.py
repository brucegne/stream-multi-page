import streamlit as st
import requests, json

st.set_page_config(page_title="Nifty Stuff",
                    page_icon=":bar_chart:",
                    layout="wide")

st.title("Welcome to StreamLit")

work_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users.json'
user_url = 'https://socialpancakes-d1dad.firebaseio.com/bdata/Users/%s.json'


form =  st.form(key='editform1234',clear_on_submit=True)
user_name = form.text_input('User Name', value='')
user_email = form.text_input('User Email', value='')
user_comments = form.text_input('Comments', value='')
usr_submit = form.form_submit_button(label="Save Changes")
if usr_submit:
    post_url = work_url
    post_data = {}
    post_data['name'] = user_name
    post_data['email'] = user_email
    post_data['comments'] = user_comments
    res = requests.post(post_url,json=post_data)


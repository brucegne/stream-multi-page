import streamlit as st

col1, col2, col3 = st.columns([1,2,1])

with col1:
    col1.header("This is on the left")
    col1.subheader("This would be a little smaller")

with col2:
    col2.header("This should be in the center")
    my_upload = st.file_uploader("Upload a local photo")
    my_image = st.camera_input("Take your picture", disabled=False)

with col3:
    col3.header("This is hanging out on the right")
    if my_image:
        st.success("You got the picture")
        st.image(my_image)
    if my_upload:
        st.image(my_upload)



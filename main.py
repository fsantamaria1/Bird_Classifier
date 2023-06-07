import streamlit as st
import time

st.title("Bird Classifier")
st.header(":bird: :turkey: :peacock: :swan:  :owl: :duck: :flamingo: :eagle: :parrot:")
st.markdown('_By Fredy Santamaria_')

bird_image = st.file_uploader("Please upload an image of a bird", type="jpg")

classify_button = st.button("Get Bird Species")
if classify_button:
    if bird_image:
        with st.spinner(text='In progress...'):
            time.sleep(5)
            st.success('Done')
    else:
        st.error('Please upload an image')

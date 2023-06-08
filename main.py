import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the bird species labels
birds_df = pd.read_csv('data/birds.csv')

# Load the trained model
model = tf.keras.models.load_model('data/models/improved_bird_model.h5')

st.title("Bird Classifier")
st.header(":bird: :turkey: :peacock: :swan:  :owl: :duck: :flamingo: :eagle: :parrot:")
st.markdown('_By Fredy Santamaria_')

bird_image = st.file_uploader("Please upload an image of a bird", type="jpg")

classify_button = st.button("Get Bird Species")
if classify_button:
    if bird_image:

        with st.spinner(text='In progress...'):
            # Preprocess image
            img = image.load_img(bird_image, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            # Perform the prediction
            predictions = model.predict(img_array)[0]
            st.success('Done')

            # Get the index of the highest predicted class
            top_index = np.argmax(predictions)
            class_id = top_index
            idx = birds_df[birds_df['class id'] == class_id].index.tolist()
            if idx:
                label = birds_df.loc[idx[0], 'labels']
                probability = predictions[top_index] * 100

        # Display the predicted class name
        st.subheader(f"Predicted Bird Species: {label}")

    else:
        st.error('Please upload an image')

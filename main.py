import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the bird species labels
birds_df = pd.read_csv('data/birds.csv')

# Load the trained model
model = tf.keras.models.load_model('data/models/tuned_bird_model.h5')

st.title("Bird Classifier")
st.header(":bird: :turkey: :peacock: :swan:  :owl: :duck: :flamingo: :eagle: :parrot:")
st.markdown('_By Fredy Santamaria_')

bird_image = st.file_uploader("Please upload an image of a bird", type="jpg")

classify_button = st.button("Get Bird Species")
if classify_button:
    if bird_image:
        img = image.load_img(bird_image, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        with st.spinner(text='In progress...'):
            # Perform the prediction
            predictions = model.predict(img_array)[0]
            st.success('Done')

        # Get the top 5 predicted classes
        top_5_indices = np.argsort(predictions)[-5:][::-1]
        top_5_class_labels = []
        top_5_probabilities = []
        for i in top_5_indices:
            class_id = i
            idx = birds_df.index[birds_df['class id'] == class_id].tolist()
            if idx:
                label = birds_df.loc[idx[0], 'labels']
                probability = predictions[i] * 100
                top_5_class_labels.append(label)
                top_5_probabilities.append(probability)

        # Create a bar graph
        fig, ax = plt.subplots()
        ax.bar(top_5_class_labels, top_5_probabilities)
        ax.set_xlabel('Species')
        ax.set_ylabel('Probability (%)')
        ax.set_title('Top 5 Predicted Bird Species')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

    else:
        st.error('Please upload an image')

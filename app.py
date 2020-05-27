import streamlit as st
import numpy as np
from PIL import Image

def pass_image_to_face_gan(original_image, glasses_toggle, gender_toggle, age_slider, pose_slider):
  # To be Implemented
  return altered_image

st.title('Face-Gan App')

st.header('Upload an Image of a Face to Manipulate')

img_file_buffer = st.file_uploader("Upload a movie poster", type=["png", "jpg", "jpeg"])

glasses_toggle = streamlit.checkbox(label='Add glasses', value=True)
gender_toggle = streamlit.checkbox(label='Change Gender', value=True)
age_slider = st.slider('Change Age', 0, 1, .5)
pose_slider = st.slider('Change Pose', 0, 1, .5)

# display image
if img_file_buffer is not None:
    original_image = np.array(Image.open(img_file_buffer))
   
    #altered_image = pass_image_to_face_gan(original_image, glasses_toggle, gender_toggle, age_slider, pose_slider)
    altered_image = original_image
   
    st.image(
        np.array(altered_image), caption=f"Processed image", use_column_width=True,
    )

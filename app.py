import streamlit as st
import numpy as np
from PIL import Image

def arguments():
  global num_image = 0

def pass_image_to_face_gan(original_image, glasses_toggle, gender_toggle, age_slider, pose_slider):
  return original_image

def load_and_save_image(img_file_buffer):
  image = Image.open(img_file_buffer)
  image.save(str(num_image)+"_image.jpg")
  num_image += 1
  return np.array(image)

def modify_image(altered_image, rotate_toggle, rotate_slider,enlarge_toggle):
  image = Image.fromarray(altered_image)
  
  if rotate_toggle:
    image = image.rotate(rotate_slider)
  if enlarge_toggle:
    width, height = image.size
    image = image.resize((width*2, height*2))

  return image
  

st.title('Face-Gan App')

st.header('Upload an Image of a Face to Manipulate')

img_file_buffer = st.file_uploader("Upload a movie poster", type=["png", "jpg", "jpeg"])

glasses_toggle = st.checkbox(label='Add glasses', value=False)
gender_toggle = st.checkbox(label='Change Gender', value=False)
age_toggle = st.checkbox(label='Add glasses', value=False)
pose_toggle = st.checkbox(label='Add glasses', value=False)

rotate_toggle = st.checkbox(label='Rotate Image', value=False)
rotate_slider = st.slider('hour', 0, 360, 90)
enlarge_toggle = st.checkbox(label='Enlarge Image', value=False)

# display image
if img_file_buffer is not None:
    original_image = load_and_save_image(img_file_buffer)
    
    altered_image = pass_image_to_face_gan(original_image, glasses_toggle, gender_toggle, age_toggle, pose_toggle)
    
    altered_image = modify_image(altered_image, rotate_toggle, enlarge_toggle)
    
    st.image(
        np.array(altered_image), caption=f"Processed image", use_column_width=True,
    )

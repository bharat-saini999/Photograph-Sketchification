import streamlit as st
from PIL import Image
import cv2

st.title("Image Upload and Processing App")

# File uploader for image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

left, right = st.columns(2)

with left:

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)


try:
    with right:
        
        image1 = cv2.imread(uploaded_file.name)

        gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

        inverted_image1 = 255 - gray_image1

        blurred1 = cv2.GaussianBlur(inverted_image1, (21, 21), 0)

        inverted_blurred1 = 255 - blurred1
        pencil_sketch1 = cv2.divide(gray_image1, inverted_blurred1, scale=256.0)

        st.image(pencil_sketch1, caption="Sketch", use_column_width=True)

except AttributeError:
        st.write("Made by BHARAT ")


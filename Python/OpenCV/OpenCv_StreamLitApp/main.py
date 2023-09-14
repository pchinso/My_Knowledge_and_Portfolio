import cv2
import streamlit as st
import numpy as np
from PIL import Image


def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright


def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img


def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr

def to_grayscale(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_image


def main_loop():

    # main screen

    st.title("OpenCV Demo App")
    st.subheader("This app allows you to play with Image filters!")
    st.text("We use OpenCV and Streamlit for this demo")

    # Image Upload
    image_file = st.file_uploader(
                        "Upload Your Image", 
                        type=['jpg', 'png', 'jpeg'])
    
    if not image_file:
        return None

    # Sidebar Controls

    # Blur Slider
    blur_rate = st.sidebar.slider(
                               "Blurring", 
                               min_value=0.5, 
                               max_value=3.5)
    # Brightness Slider
    brightness_amount = st.sidebar.slider(
                                       "Brightness", 
                                       min_value=-50, 
                                       max_value=50, 
                                       value=0)
    # HDR Enhancement
    apply_enhancement_filter = st.sidebar.checkbox('Enhance Details', value=True)
    # Grayscale OOP
    apply_grayscale = st.sidebar.checkbox('To GrayScale',value=True)
    

    # Streamlit app operations
    
    # Open Image
    original_image = Image.open(image_file)
    original_image = np.array(original_image)

    # Slider operations
    processed_image = blur_image(original_image, blur_rate)

    processed_image = brighten_image(processed_image, brightness_amount)

    # Checkbox operations
    if apply_enhancement_filter:
        processed_image = enhance_details(processed_image)

    if apply_grayscale:
        processed_image = to_grayscale(processed_image)

    st.text("Original Image vs Processed Image")
    st.image([original_image, processed_image])


if __name__ == '__main__':
    main_loop()
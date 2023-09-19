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

def mouse_crop(event, x, y, flags, param):
    global refPt, cropping  # Declare refPt and cropping as global

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(processed_image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", processed_image)


def img_ROI(img):

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", img)
        key = cv2.waitKey(1) & 0xFF
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            img = processed_image.copy()
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break
    # if there are two reference points, then crop the region of interest
    # from teh image and display it
    if len(refPt) == 2:
        roi = processed_image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)
    # close all open windows
    cv2.destroyAllWindows()

    return roi




def main_loop():
    global processed_image, original_image, refPt, cropping
    refPt = []
    cropping = False

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
    # Create a checkbox in the main section to toggle the sidebar controls
    disable_sidebar_controls = False

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
    # Crop ROI
    apply_ROI = st.sidebar.checkbox('Crop ROI',value=False)
        

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

    if apply_ROI:
        processed_image = img_ROI(processed_image)
        disable_sidebar_controls = True

    st.text("Original Image vs Processed Image")
    st.image([original_image, processed_image])


if __name__ == '__main__':
    main_loop()
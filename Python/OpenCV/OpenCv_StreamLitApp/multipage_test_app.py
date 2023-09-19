import cv2
import streamlit as st
import numpy as np
from PIL import Image

# Create a dictionary to store the pages and their content
pages = {
    "Page 1": {
        "content": "This is Page 1 content.",
        "image": "images/Me_profile_pic.jpeg",  # Path to the image for Page 1
        "prev": None,
        "next": "Page 2",
    },
    "Page 2": {
        "content": "This is Page 2 content.",
        "image": "images/Me_profile_pic.jpeg",  # Path to the image for Page 2
        "prev": "Page 1",
        "next": "Page 3",
    },
    "Page 3": {
        "content": "This is Page 3 content.",
        "image": "images/Me_profile_pic.jpeg",  # Path to the image for Page 2
        "prev": "Page 2",
        "next": None,
    },
}

def blur_image(image, amount):
    blur_img = cv2.GaussianBlur(image, (11, 11), amount)
    return blur_img

def draw_page_functionalities(state):
    if 'Page1':
      image_file = pages[st.session_state.page_num]["image"]
      original_image = Image.open(image_file)
      original_image = np.array(original_image)
      # Blur Slider
      blur_rate = st.sidebar.slider(
                            "Blurring", 
                            min_value=0.5, 
                            max_value=3.5)
      processed_image = blur_image(original_image, blur_rate)

    if processed_image is not None:
        # Display the uploaded image
        st.image(processed_image, caption="Uploaded Image", use_column_width=True)

    with open('./Me_profile_pic.jpeg', "wb") as f:
        f.write(processed_image)

    pages[st.session_state.page_num]["image"] = processed_image
    
    if 'Page2':
        blur_rate = False

        


# Define a session state variable to keep track of the current page
if "page_num" not in st.session_state:
    st.session_state.page_num = "Page 1"
    

# Define the Streamlit app
def main():
    st.title("Multi-Page Streamlit App")

    # Update the sidebar radio buttons based on the current page
    page_names = list(pages.keys())
    selected_page_index = page_names.index(st.session_state.page_num)
    selected_page_index = st.sidebar.radio("Select Page", page_names, selected_page_index)

    # Set the current page based on the selection
    st.session_state.page_num = selected_page_index

    # Display the content of the selected page
    st.write(pages[st.session_state.page_num]["content"])

    # Display the image of the selected page
    image_path = pages[st.session_state.page_num]["image"]
    st.image(image_path, caption=f"Image for {st.session_state.page_num}", use_column_width=True)
    draw_page_functionalities(st.session_state.page_num)

    # Create a column layout for the navigation buttons at the bottom
    col1, col2, col3 = st.columns([1, 5, 1])

    # Navigation buttons
    if pages[st.session_state.page_num]["prev"]:
        if col1.button("Previous"):
            st.session_state.page_num = pages[st.session_state.page_num]["prev"]
            st.experimental_rerun()
    if pages[st.session_state.page_num]["next"]:
        if col3.button("Next"):
            st.session_state.page_num = pages[st.session_state.page_num]["next"]
            st.experimental_rerun()


if __name__ == "__main__":
    main()
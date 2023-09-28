import cv2
import streamlit as st
import numpy as np
from PIL import Image


class StreamlitApp:
    def __init__(self):
        self.current_screen = None
        self.screens = ["Home", 
                        "About", 
                        "Contact",
                        ]
        
        self.screens = [
        {
        'title': 'Upload',
        'header': 'Upload image',
        'write': 'Upload a image to edit',
        'image': '',
        'image_caption': 'Original Image',
        },
        {
        'title': 'About',
        'header': 'About Screen',
        'write': 'This is the about screen.',
        'image': 'images/Me_profile_pic.jpeg',
        'image_caption': 'About image',
        },
        {
        'title': 'Contact',
        'header': 'Contact Screen',
        'write': 'You can contact us at contact@example.com',
        'image': 'images/Me_profile_pic.jpeg',
        'image_caption': 'Contact image',
        },
        {
        'title': 'Send',
        'header': 'Send Results',
        'write': 'Sending results to contact@example.com',
        'image': '',
        'image_caption': 'No Image',
        },        
        ]

        self.radio_buttons = [screen['title'] for screen in self.screens]


        self.navigation = st.sidebar.radio("Select Screen", 
                                           self.radio_buttons
                                           )

    def run(self):

        # Main App Title
        st.title("Object-Oriented Streamlit App")
        
        self.show_screen()
            


    def show_screen(self):

        # Index of actual navigation button selected
        screen_index = next((
        screen_index
        for screen_index, screen in enumerate(self.screens)
        if screen['title'] == self.navigation
        ), None)   

        # Shows screen data
        st.header(self.screens[screen_index]['header'])
        st.write(self.screens[screen_index]['write'])
        
        if self.screens[screen_index]['image'] != '':
            try:
                st.image(self.screens[screen_index]['image'], 
                        caption=self.screens[screen_index]['image_caption']
                        )
                
            except FileNotFoundError:
                st.error("File not found. Please provide a valid file path.")      

            
        # Update current screen
        self.current_screen = screen_index

        if self.current_screen == 0: # Upload

            # Image Upload
            image_file = st.file_uploader(
                                "Upload Your Image", 
                                type=['jpg', 'png', 'jpeg'])            
            
            self.screens[screen_index]['image'] = image_file

            if self.screens[screen_index]['image'] != '':
                original_image = Image.open(self.screens[screen_index]['image'])
                original_image = np.array(original_image)            




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

    app = StreamlitApp()
    app.run()
import streamlit as st

class StreamlitApp:
    def __init__(self):
        self.current_screen = None
        self.screens = ["Home", 
                        "About", 
                        "Contact",
                        ]
        self.navigation = st.sidebar.radio("Select Screen", self.screens)

    def run(self):
        st.title("Object-Oriented Streamlit App")
        self.show_navigation()

    def show_navigation(self):
                
        if self.navigation in self.screens:
            self.show_screen()


    def show_screen(self):

        if self.navigation == "Home":
            st.header("Home Screen")
            st.write("Welcome to the home screen!")
            st.image("images/Me_profile_pic.jpeg", caption="Home Image")

        elif self.navigation == "About":
            st.header("About Screen")
            st.write("This is the about screen.")
            st.image("images/Me_profile_pic.jpeg", caption="About Image")            

        elif self.navigation == "Contact":
            st.header("Contact Screen")
            st.write("You can contact us at contact@example.com")
            st.image("images/Me_profile_pic.jpeg", caption="Contact Image")            


if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
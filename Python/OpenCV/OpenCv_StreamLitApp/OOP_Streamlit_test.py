import streamlit as st

class StreamlitApp:
    def __init__(self):
        self.current_screen = None

    def run(self):
        st.title("Object-Oriented Streamlit App")
        self.show_navigation()

    def show_navigation(self):
        navigation = st.sidebar.radio("Select Screen", ["Home", "About", "Contact"])
        if navigation == "Home":
            self.show_home()
        elif navigation == "About":
            self.show_about()
        elif navigation == "Contact":
            self.show_contact()

    def show_home(self):
        st.header("Home Screen")
        st.write("Welcome to the home screen!")
        st.image("images/Me_profile_pic.jpeg", caption="Home Image")

    def show_about(self):
        st.header("About Screen")
        st.write("This is the about screen.")
        st.image("images/Me_profile_pic.jpeg", caption="About Image")

    def show_contact(self):
        st.header("Contact Screen")
        st.write("You can contact us at contact@example.com")
        st.image("images/Me_profile_pic.jpeg", caption="Contact Image")

if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
"""Welcome to Reflex!."""

from links_web import styles

# Import all the pages.
from links_web.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style, stylesheets=["fonts/myfont.css"])
app.compile()

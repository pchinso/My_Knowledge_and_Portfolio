"""The home page of the app."""

from links_web import styles
from links_web.templates import template

import reflex as rx


@template(route="/", title="Upload", image="/upload.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    # return rx.markdown(content, component_map=styles.markdown_style)

    return rx.upload(
        rx.text(
            "Drag and drop files here or click to select files"
        ),
        border="1px dotted rgb(107,99,246)",
        padding="5em",
    )

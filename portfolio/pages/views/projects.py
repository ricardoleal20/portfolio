"""Include a Projects View"""

import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.components.table import create_table_component
# Data import
from portfolio.data import PROJECTS


def projects():
    """Project view option"""
    return rx.box(
        section_header_icon(
            "code",
            "Projects"
        ),
        rx.box(
            rx.text(
                "The following projects have been developed to showcase my" +
                " proficiency with various tools, for personal enjoyment," +
                " or to address specific problems. You can see them displayed" +
                " in the table below.",
                size="4"
            ),
            margin_top="1em",
        ),
        __body_projects(),
        # __body_vstack_projects(),
        id="projects",
        width="100%"
    )

# Create the method for the projects


def __body_projects() -> rx.Component:
    """Create the body for the projects section"""
    data = [{
        "Project Title": {
            "value": project.project_title,
            # Include the extra info styling
            "width": "320px",
            "max_width": "320px",
            "white_space": "normal",
            "word_wrap": "break-word"
        },
        "Description": {
            "value": rx.text(
                project.description,
                size="1",
                weight="medium"
            ),
            # Include the extra info styling
            "width": "320px",
            "max_width": "320px",
            "white_space": "normal",
            "word_wrap": "break-word"
        },
        "Software Skills": project.software_skills,
        "Link": rx.link(
            rx.hstack(
                rx.icon("link", size=15),
                rx.text("Visit"),
                spacing="1"
            ),
            href=project.url_project,
            size="1",
            color=rx.color("blue", 11),
            weight="bold",
            underline="hover",
        ) if project.url_project else "N/A",
        "Source Code": rx.link(
            rx.hstack(
                rx.icon("github", size=15),
                rx.text("Source Code"),
                spacing="1"
            ),
            href=project.url_github,
            size="1",
            color=rx.color("blue", 11),
            weight="bold",
            underline="hover",
        ) if project.url_github else "N/A",
    } for project in PROJECTS]
    # Create the table component
    return rx.center(
        create_table_component(data, max_width="85%"),
        margin_top="1.5em",
        width="100%"
    )

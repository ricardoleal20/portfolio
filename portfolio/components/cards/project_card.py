"""
Define the Project card to define different projects
"""
import reflex as rx
# Local imports
from portfolio.models import ProjectModel
from portfolio.styles import (
    TextSizes
)
from portfolio.components.skills import hstack_software_tags
from portfolio.components.miscellaneous import main_button


def project_card(model: ProjectModel):
    """Define the project card element with the desktop and mobile
    alternatives
    """
    return rx.box(
        rx.desktop_only(
            __desktop_project_card(model)
        ),
        rx.mobile_and_tablet(
            __mobile_tablet_project_card(model)
        )
    )


def __desktop_project_card(model: ProjectModel):
    """Define the Desktop alternative"""
    return rx.hstack(
        rx.image(
            src=model.project_image,
            width="550px",
            height="317px",
            border_radius="15px"
        ),
        rx.flex(
            rx.vstack(
                rx.text(
                    model.project_title,
                    font_size=TextSizes.HEADING_H3.value,
                    weight="bold"
                ),
                hstack_software_tags(model.software_skills),
                rx.text(
                    model.description,
                    font_size=TextSizes.HEADING_H3.value,
                ),
                rx.hstack(
                    main_button(
                        "github",
                        "Code",
                        model.url_github,
                        size_str="3"
                    ),
                    main_button(
                        "link",
                        "Visitar",
                        model.url_project,
                        size_str="3"
                    ),
                    spacing="6"
                )
            ),
        ),
        spacing="9",
        align="center",
    )


def __mobile_tablet_project_card(model: ProjectModel):
    """Define the mobile alternatives"""
    return rx.vstack(
        rx.image(
            src=model.project_image,
            width="100%",
            height="auto",
            border_radius="15px"
        ),
        rx.flex(
            rx.vstack(
                rx.text(
                    model.project_title,
                    font_size=TextSizes.HEADING_H3.value,
                    weight="bold"
                ),
                hstack_software_tags(model.software_skills),
                rx.text(
                    model.description,
                    font_size=TextSizes.HEADING_H3.value,
                ),
                rx.hstack(
                    main_button(
                        "github",
                        "Code",
                        model.url_github,
                        size_str="3"
                    ),
                    main_button(
                        "link",
                        "Visite",
                        model.url_project,
                        size_str="3"
                    ),
                    spacing="6"
                )
            ),
        ),
        spacing="3",
        align="center",
    )

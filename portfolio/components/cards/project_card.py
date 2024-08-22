"""
Define the Project card to define different projects
"""
import reflex as rx
# Local imports
from portfolio.models import ProjectModel, OpenSourceModel
from portfolio.styles import (
    TextSizes
)
from portfolio.components.skills import hstack_software_tags
from portfolio.components.miscellaneous import main_button


def project_card(model: ProjectModel | OpenSourceModel):
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


def __desktop_project_card(model: ProjectModel | OpenSourceModel):
    """Define the Desktop alternative"""

    cards: list[rx.Component] = []
    if model.project_image:
        cards.append(rx.image(
            src=model.project_image,
            width="550px",
            height="317px",
            border_radius="15px"
        ))
    cards.append(rx.flex(
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
                *__project_buttons(model),
                spacing="6"
            )
        ),
    ))

    return rx.hstack(
        *cards,
        spacing="9",
        align="center",
    )


def __mobile_tablet_project_card(model: ProjectModel | OpenSourceModel):
    """Define the mobile alternatives"""
    cards: list[rx.Component] = []

    if model.project_image:
        cards.append(rx.image(
            src=model.project_image,
            width="100%",
            height="auto",
            border_radius="15px"
        ))
    cards.append(rx.flex(
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
                    *__project_buttons(model),
                    spacing="6"
                )
            ),
    ))

    return rx.vstack(
        *cards,
        spacing="3",
        align="center",
    )


def __project_buttons(model: ProjectModel | OpenSourceModel):
    """Return the project buttons"""
    buttons = []
    # If we have the github button, add them as button
    if model.url_github:
        buttons.append(
            main_button(
                "github",
                "Code",
                model.url_github,
                size_str="3"
            ))
    if model.url_project:
        buttons.append(
            main_button(
                "link",
                "Visit",
                model.url_project,
                size_str="3"
            )
        )
    # Return the buttons
    return buttons

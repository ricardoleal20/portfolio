"""Include a Projects View"""

import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.components.cards.project_card import project_card
# Data import
from portfolio.data import PROJECTS


def projects():
    """Project view option"""
    return rx.box(
        section_header_icon(
            "code",
            "Projects"
        ),
        __body_vstack_projects(),
        id="projects"
    )


def __body_vstack_projects():
    """Body Stack for the projects"""
    return rx.vstack(
        *[
            project_card(model)
            for model in PROJECTS
        ],
        spacing="9",
        margin_top="4em"
    )

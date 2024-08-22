"""Include an Open Source View"""

import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.components.cards.project_card import project_card
# Data import
from portfolio.data import OPEN_SOURCE


def open_source():
    """Project view option"""
    return rx.box(
        section_header_icon(
            "git-compare-arrows",
            "Open Source projects"
        ),
        __body_vstack_projects(),
        id="open_source"
    )


def __body_vstack_projects():
    """Body Stack for the open source code"""
    return rx.vstack(
        *[
            project_card(model)
            for model in OPEN_SOURCE
        ],
        spacing="9",
        margin_top="4em"
    )

"""
Laboral Experience view
"""
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.components.cards.work_card import work_experience_card
# Data import
from portfolio.data import WORK_EXPERIENCE


def laboral_experience():
    """Laboral experience information"""
    return rx.box(
        section_header_icon(
            "briefcase-business",
            "Work experience"
        ),
        __body_vstack_experience(),
        id="experience",
    )


def __body_vstack_experience():
    """VStack with all the projects stored"""
    return rx.vstack(
        *[
            work_experience_card(model)
            for model in WORK_EXPERIENCE
        ],
        margin_top="4em",
        spacing="9"
    )

"""
Education view for the project
"""
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.components.cards.education_card import education_card
from portfolio.models import EducationalModel
# Data import
from portfolio.data import EDUCATION, CERTIFICATES


def education():
    """Add the education view for the page"""
    return rx.box(
        section_header_icon(
            "graduation-cap",
            "Education"
        ),
        __body_hstack_education(EDUCATION),
        id="education"
    )


def certificates():
    """Add the education view for the page"""
    return rx.box(
        section_header_icon(
            "book-headphones",
            "Certificates"
        ),
        __body_hstack_education(CERTIFICATES),
        id="certificates"
    )


def __body_hstack_education(models: list[EducationalModel]):
    """Body stack for the education"""
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                *[
                    education_card(model, len(models))
                    for model in models
                ],
                spacing="7",
                margin_top="3em"
            )
        ),
        rx.mobile_and_tablet(
            rx.vstack(
                *[
                    education_card(model, 1)
                    for model in models
                ],
                spacing="7",
                margin_top="3em"
            )
        )
    )

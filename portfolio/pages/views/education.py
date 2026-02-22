"""
Education view for the project
"""
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.components.cards.education_card import education_card, certificate_row
from portfolio.components.table import create_table_component
# Data import
from portfolio.data import EDUCATION, CERTIFICATES


def education():
    """Add the education view for the page"""
    return rx.box(
        section_header_icon("graduation-cap", "Education"),
        rx.vstack(
            *[education_card(model) for model in EDUCATION],
            spacing="0",
            margin_top="3em",
            width="100%",
        ),
        id="education"
    )


def certificates():
    """Add the education view for the page"""
    return rx.box(
        section_header_icon("book-headphones", "Certificates"),
        rx.box(
            create_table_component(
                [certificate_row(model) for model in CERTIFICATES],
                max_width="100%",
            ),
            margin_top="3em",
        ),
        id="certificates"
    )

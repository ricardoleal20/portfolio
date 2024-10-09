"""
Include a card for my education
"""
import reflex as rx
# Local imports
from portfolio.models import EducationalModel
from portfolio.styles import TextSizes, Color
# Locally import the main button
from portfolio.components.miscellaneous import main_button


def education_card(model: EducationalModel):
    """Include the education card"""
    # Define the study object ONLY if they have url
    return rx.card(
        rx.vstack(
            rx.icon(
                model.education_type.value,
                size=30
            ),
            rx.text(
                model.study_subject,
                font_size=TextSizes.HEADING_H3.value,
                color=Color.PRIMARY.value,
                weight="bold",
                align="center"
            ),
            rx.text(
                model.range_years,
                font_size=TextSizes.CARD_BODY.value,
            ),
            rx.text(
                model.description,
                font_size=TextSizes.CARD_BODY.value,
                text_align="center"
            ),
            # Add an URL button only if we have one
            rx.cond(
                bool(model.url),
                main_button("link", "See", model.url, "3")  # type: ignore
            ),
            align="center",
            justify="center",
            padding_y="2em"
        )
    )

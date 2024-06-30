"""
Include a card for my education
"""
import reflex as rx
# Local imports
from portfolio.models import EducationalModel
from portfolio.styles import TextSizes, Color


def education_card(model: EducationalModel):
    """Include the education card"""
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
            align="center",
            justify="center",
            padding_y="2em"
        )
    )

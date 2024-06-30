"""
Include a card for my education
"""
import reflex as rx
# Local imports
from portfolio.models import EducationalModel, EducationalType
from portfolio.styles import TextSizes, Color


def education_card(model: EducationalModel):
    """Include the education card"""
    return rx.card(
        rx.vstack(
            rx.icon(
                __get_icon_by_education_type(model.education_type),
                size=30
            ),
            rx.text(
                model.study_subject,
                font_size=TextSizes.HEADING_H3.value,
                color=Color.PRIMARY.value,
                weight="bold"
            ),
            rx.text(
                model.education_type,
                font_size=TextSizes.CARD_HEADER.value,
                weight="regular"
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


def __get_icon_by_education_type(education_type: EducationalType):
    if education_type == EducationalType.UNIVERSITY.value:
        return "university"
    if education_type == EducationalType.LANGUAGE.value:
        return "languages"
    if education_type == EducationalType.CERTIFICATE.value:
        return "file-badge"
    return "file-badge"

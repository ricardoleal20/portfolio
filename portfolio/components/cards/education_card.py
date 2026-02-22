"""
Include a card for my education
"""
import reflex as rx
# Local imports
from portfolio.models import EducationalModel
from portfolio.styles import TextSizes, Color
from portfolio.components.miscellaneous import main_button


def education_card(model: EducationalModel, _number_of_cards: int = 2):
    """Timeline-style row for an education entry"""
    return rx.hstack(
        # Left: icon in a circle
        rx.box(
            rx.icon(model.education_type.value, size=22, color=Color.PRIMARY.value),
            padding="0.6em",
            border=f"2px solid {Color.PRIMARY.value}",
            border_radius="50%",
            flex_shrink="0",
        ),
        # Right: content
        rx.vstack(
            rx.hstack(
                rx.text(
                    model.study_subject,
                    font_size=TextSizes.HEADING_H3.value,
                    color=Color.PRIMARY.value,
                    weight="bold",
                ),
                rx.spacer(),
                rx.badge(
                    model.range_years,
                    color_scheme="green",
                    variant="soft",
                    size="1",
                ),
                align="center",
                width="100%",
            ),
            rx.text(
                model.educational_entity,
                font_size=TextSizes.CARD_BODY.value,
                color="var(--gray-11)",
                font_style="italic",
            ),
            rx.text(
                model.description.strip(),
                font_size=TextSizes.CARD_BODY.value,
                color="var(--gray-11)",
            ),
            rx.cond(
                bool(model.url),
                main_button("link", "See certificate", model.url, "2"),  # type: ignore
            ),
            spacing="1",
            align="start",
            width="100%",
        ),
        align="start",
        spacing="5",
        width="100%",
        padding="1.2em",
        border_left="3px solid var(--gray-4)",
        _hover={"border_left": f"3px solid {Color.PRIMARY.value}"},
        transition="border-left 0.2s ease",
    )


def certificate_card(model: EducationalModel):
    """Compact badge-style card for certificates"""
    return rx.card(
        rx.hstack(
            rx.icon(model.education_type.value, size=20, color=Color.PRIMARY.value),
            rx.vstack(
                rx.text(
                    model.study_subject,
                    font_size=TextSizes.CARD_BODY.value,
                    weight="bold",
                    color=Color.PRIMARY.value,
                ),
                rx.text(
                    model.educational_entity,
                    font_size="0.85em",
                    color="var(--gray-11)",
                ),
                rx.badge(
                    model.range_years,
                    color_scheme="green",
                    variant="soft",
                    size="1",
                ),
                spacing="1",
                align="start",
            ),
            spacing="3",
            align="start",
        ),
        rx.cond(
            bool(model.url),
            rx.box(
                main_button("link", "See certificate", model.url, "2"),  # type: ignore
                margin_top="0.8em",
            ),
        ),
        padding="1em",
        width="100%",
    )

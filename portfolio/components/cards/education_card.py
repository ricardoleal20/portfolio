"""
Include a card for my education
"""
import reflex as rx
# Local imports
from portfolio.models import EducationalModel
from portfolio.styles import TextSizes, Color
# Locally import the main button
from portfolio.components.miscellaneous import main_button


def education_card(model: EducationalModel, number_of_cards: int = 2):
    """Include the education card"""
    # SELECT THE WIDTH OF THE CARD!
    width = f"{100/number_of_cards}%"
    # Only if we have number of cards = 1, we'll change the height
    if number_of_cards == 1:
        # Depending on the len of characters...
        if len(model.description) > 1100:
            height = "60em"
        elif len(model.description) > 950:
            height = "50em"
        elif len(model.description) > 600:
            height = "40em"
        else:
            height = "30em"
    else:
        height = "38em"
    # Define the study object ONLY if they have url
    return rx.card(
        rx.hstack(
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
                    main_button("link", "See certificate",
                                model.url, "3")  # type: ignore
                ),
                align="center",
                justify="center",
                padding_y="2em",
            ),
            rx.box(
                background_size="16px 16px",
                background_image=f"radial-gradient(circle, {rx.color('gray', 12)}" +
                " 0.3px, transparent 0.5px)",
                mask="radial-gradient(100% 100% at 100% 100%, " +
                "hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
                width="100%",
                height="100%",
                position="absolute",
            )
        ),
        height=height,
        width=width,
    )

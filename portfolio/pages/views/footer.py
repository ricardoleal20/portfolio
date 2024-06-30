"""
Footer view for the page
"""
import reflex as rx
# Local imports
from portfolio.styles import TextSizes, Color, border_spacer
from portfolio import __info__ as info
from portfolio.components.miscellaneous import link_icons


def footer():
    """Footer view"""
    return rx.box(
        rx.vstack(
            rx.text(
                info.FULL_NAME,
                font_size=TextSizes.HEADING_H3.value,
                weight="bold"
            ),
            rx.link(
                rx.text(
                    info.EMAIL.replace("mailto:", ""),
                    font_size=TextSizes.LINKS_TEXT.value,
                    weight="medium",
                    color=Color.PRIMARY.value
                ),
                href=info.EMAIL,
                text_decoration="none"
            ),
            rx.hstack(
                link_icons("linkedin", info.URL_LINKED_IN, 25),
                link_icons("github", info.URL_GITHUB, 25),
                spacing="5"
            ),
            rx.box(
                rx.text(
                    "Made by ",
                    display="inline"
                ),
                rx.link(
                    rx.color_mode_cond(
                        light=rx.text(
                            info.FULL_NAME,
                            display="inline",
                            color=Color.TEXT.value
                        ),
                        dark=rx.text(
                            info.FULL_NAME,
                            display="inline",
                            color=Color.TEXT_SECONDARY.value
                        ),
                    ),
                    href=info.URL_GITHUB,
                    is_external=True,
                    text_decoration="none"
                ),
                rx.text(
                    " with love and the help of his cat.",
                    display="inline"
                ),
                display="inline"
            ),
            justify="center",
            align="center"
        ),
        border_top=border_spacer,
        width="100%",
        padding_y="3em"
    )

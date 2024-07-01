"""
Welcome section!
"""
import reflex as rx
# Local imports
from portfolio.styles import TextSizes
from portfolio import __info__ as info
from portfolio.components.miscellaneous import (
    main_button, secondary_button, link_icons
)


def welcome():
    """Welcome home information for the index project"""
    return rx.center(
        rx.desktop_only(
            __desktop_welcome_home()
        ),
        rx.tablet_only(
            __table_welcome_home()
        ),
        rx.mobile_only(
            __mobile_welcome_home()
        ),
        min_height="70vh",
    )


def __desktop_welcome_home():
    """Desktop view for the Welcome home"""
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.heading(
                    info.FULL_NAME,
                    font_size=TextSizes.HEADING_H1.value,
                    as_="h1",
                    line_height="1.2em"
                ),
                rx.text(
                    info.PROFESSION,
                    font_size=TextSizes.HEADING_H2.value,
                    weight="regular"
                ),
                rx.text(
                    info.DESCRIPTION,
                    font_size=TextSizes.BODY_HOME_TEXT.value,
                    as_="p"
                ),
                rx.hstack(
                    link_icons("linkedin", info.URL_LINKED_IN, 35),
                    link_icons("github", info.URL_GITHUB, 35),
                    spacing="5"
                ),
                rx.hstack(
                    main_button(
                        "download",
                        "Download CV",
                        info.URL_CV,
                        "4"
                    ),
                    secondary_button(
                        "mail",
                        "Contact me",
                        info.EMAIL,
                        "4"
                    ),
                    spacing="5"
                )
            ),
            rx.image(
                src="/profile.jpeg",
                width="auto",
                height="22vw",
                border_radius="30px"
            ),
            align="center",
            spacing="7"
        )
    )


def __table_welcome_home():
    """Table view for the Welcome home"""
    return rx.box(
        rx.vstack(
            rx.image(
                src="/profile.jpeg",
                width="auto",
                height="270px",
                border_radius="30px"
            ),
            rx.vstack(
                rx.heading(
                    info.FULL_NAME,
                    font_size=TextSizes.HEADING_H1.value,
                    as_="h1",
                    line_height="1.2em"
                ),
                rx.text(
                    info.PROFESSION,
                    font_size=TextSizes.HEADING_H2.value,
                    weight="regular"
                ),
                rx.text(
                    info.DESCRIPTION,
                    font_size=TextSizes.BODY_HOME_TEXT.value,
                    as_="p"
                ),
                rx.hstack(
                    link_icons("linkedin", info.URL_LINKED_IN, 35),
                    link_icons("github", info.URL_GITHUB, 35),
                    spacing="5"
                ),
                rx.hstack(
                    main_button(
                        "download",
                        "Download CV",
                        info.URL_CV,
                        "4"
                    ),
                    secondary_button(
                        "mail",
                        "Contact me",
                        info.EMAIL,
                        "4"
                    ),
                    spacing="6"
                )
            ),
            align="center",
            spacing="7",
        ),
        margin_top="3em"
    )


def __mobile_welcome_home():
    """Mobile view for the Welcome home"""
    return rx.box(
        rx.vstack(
            rx.image(
                src="/profile.jpeg",
                width="auto",
                height="270px",
                border_radius="30px"
            ),
            rx.vstack(
                rx.heading(
                    info.FULL_NAME,
                    font_size=TextSizes.HEADING_H1_MOBILE.value,
                    as_="h1",
                    line_height="1.2em",
                    text_align="center"
                ),
                rx.text(
                    info.PROFESSION,
                    font_size=TextSizes.HEADING_H2_MOBILE.value,
                    weight="regular",
                    text_align="center",
                    width="100%"
                ),
                rx.text(
                    info.DESCRIPTION,
                    font_size=TextSizes.BODY_HOME_TEXT_MOBILE.value,
                    as_="p"
                ),
                rx.hstack(
                    link_icons("linkedin", info.URL_LINKED_IN, 25),
                    link_icons("github", info.URL_GITHUB, 25),
                    spacing="5",
                    justify="center",
                    align="center",
                    width="100%"
                ),
                rx.vstack(
                    main_button(
                        "download",
                        "Download CV",
                        info.URL_CV,
                        "4"
                    ),
                    secondary_button(
                        "mail",
                        "Contact me",
                        info.EMAIL,
                        "4"
                    ),
                    spacing="4",
                    justify="center",
                    align="center",
                    width="100%"
                )
            ),
            align="center",
            spacing="7"
        ),
        margin_top="3em"
    )

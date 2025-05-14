"""
Different and minor components that can be helpful

In those components, we include things such as buttons, links and other things
"""
from typing import Literal
import reflex as rx
# Local imports
from portfolio.styles import (
    TextSizes, Color,
    main_button_style, secondary_button_style,
    text_could_hover, button_secondary_hover
)


# ======================================== #
#                  BUTTONS                 #
# ======================================== #

def main_button(
    icon_str: str,
    text: str,
    url_str: str,
    size_str: Literal["1", "2", "3", "4"]
):
    """Main button"""
    return rx.link(
        rx.button(rx.icon(icon_str), text, size=size_str, style=main_button_style),
        href=url_str,
        is_external=True,
        z_index=1,
    )


def secondary_button(
    icon_str: str,
    text: str,
    url_str: str,
    size_str: Literal["1", "2", "3", "4"]
):
    """Secondary button."""
    return rx.link(
        rx.button(
            rx.icon(
                icon_str
            ),
            text,
            size=size_str,
            style=secondary_button_style
        ),
        href=url_str,
    )

# ======================================== #
#                  ICONS                   #
# ======================================== #


def link_icons(
    icon_str: str,
    url: str,
    size: int
):
    """Link component for be inside of an Icon."""
    return rx.link(
        rx.icon(
            icon_str,
            size=size,
            color=rx.color_mode_cond(light="black", dark="white")
        ),
        href=url,
        is_external=True
    )

# ======================================== #
#                 NAVBAR                   #
# ======================================== #


def navbar_link(
    text: str,
    id_scroll: str
):
    """Include a link for the Navigation Bar"""
    return rx.link(
        rx.text(
            text,
            style=text_could_hover
        ),
        text_decoration="none",
        color=rx.color_mode_cond(light="black", dark="white"),
        on_click=rx.scroll_to(id_scroll),
    )


def navbar_menu_item_link(text: str, id_scroll: str):
    """Include a menu item with a link in the Navigation Bar"""
    return rx.menu.item(
        text,
        style=button_secondary_hover,
        on_click=rx.scroll_to(id_scroll),
    )

# ======================================== #
#                PARAGRAPH                 #
# ======================================== #


def paragraph_normal_and_bold(*args: str):
    """Paragraph of more than one 1 argument.
    Include :bold: to make the text bold.
    """
    return rx.box(
        *[
            bold_text(arg)
            if (
                arg.startswith(":bold:")
            ) else
            normal_text(arg)
            for arg in args
        ],
        display="inline"
    )


def normal_text(text: str):
    """Print normal text here"""
    return rx.text(
        text,
        display="inline",
        font_size=TextSizes.BODY_HOME_TEXT.value
    )


def bold_text(text: str):
    """Print bold text in this situation"""
    return rx.text(
        text[6:],
        weight="bold",
        display="inline",
        color=Color.PRIMARY.value,
        font_size=TextSizes.BODY_HOME_TEXT.value
    )

# ======================================== #
#                SECTION                   #
# ======================================== #


def section_header_icon(icon_str: str, text_heading: str):
    """Add an icon to the header of a section"""
    return rx.hstack(
        rx.icon(
            icon_str,
            size=40
        ),
        rx.text(
            text_heading,
            font_size=TextSizes.SECTION_HEADING.value,
            line_height="1.2em",
            weight="bold"
        ),
        spacing="6"
    )

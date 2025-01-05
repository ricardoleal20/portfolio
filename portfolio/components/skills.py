"""
Include the Skills as Software Engineer
"""
import reflex as rx
from portfolio.styles import (
    TextSizes, Color
)


def tag_software_skill(software_str: str):
    """Include a tag as Software Skills"""
    return rx.box(
        rx.text(
            software_str,
            font_size=TextSizes.LINKS_TEXT.value,
            color=Color.PRIMARY,
            weight="bold",
            padding_x="1em",
            padding_y="0.5em"
        ),
        border_radius="15px",
        background_color=Color.GREY,
    )


def hstack_software_tags(software_skills):
    """Define the little box for the software Tags"""
    return rx.flex(
        *[
            tag_software_skill(software)
            for software in software_skills
        ],
        wrap="wrap",
        spacing="5"
    )

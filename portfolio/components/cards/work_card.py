"""
Include a card for the Work Experience
"""
import reflex as rx
# Local imports
from portfolio.models import WorkExperienceModel
from portfolio.styles import TextSizes, Color
from portfolio.components.skills import hstack_software_tags


def work_experience_card(model: WorkExperienceModel):
    """Timeline-style card for a work experience entry"""
    return rx.hstack(
        # Timeline blip
        rx.box(
            rx.box(
                width="12px",
                height="12px",
                border_radius="50%",
                background=Color.PRIMARY.value,
                position="relative",
                left="-6px",
                top="6px",
            ),
            border_left="2px solid var(--gray-4)",
            padding_left="0",
            flex_shrink="0",
            min_height="100%",
        ),
        # Content
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        model.position_job,
                        size="4",
                        weight="bold",
                        color=Color.PRIMARY.value,
                    ),
                    rx.text(
                        model.company_and_city,
                        size="2",
                        color="var(--gray-11)",
                    ),
                    spacing="0",
                    align="start",
                ),
                rx.spacer(),
                rx.badge(
                    model.worked_date,
                    color_scheme="green",
                    variant="soft",
                    size="1",
                ),
                align="start",
                width="100%",
                wrap="wrap",
            ),
            rx.text(
                model.description_job.strip(),
                font_size=TextSizes.CARD_BODY.value,
                color="var(--gray-11)",
            ),
            hstack_software_tags(model.software_skills),
            spacing="3",
            align="start",
            width="100%",
            padding_bottom="2em",
        ),
        align="start",
        spacing="4",
        width="100%",
    )

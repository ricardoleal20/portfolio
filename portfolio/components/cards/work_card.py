"""
Include a card for the Work Experience
"""
import reflex as rx
# Local imports
from portfolio.models import WorkExperienceModel
from portfolio.styles import TextSizes
from portfolio.components.skills import hstack_software_tags


def work_experience_card(model):
    """Include a card for the Work Experience"""
    return rx.box(
        rx.tablet_and_desktop(
            __desktop_tablet_work_experience(model),
            border_left=f"1px solid {rx.color('gray', 5)}",
            # spacing="7"
        ),
        rx.mobile_only(
            __mobile_work_experience(model)
        ),
    )


def __blip():
    """Create a blip for the Timeline of the Work Experience"""
    return rx.box(
        width="10px",
        height="10px",
        border_radius="10px",
        background=rx.color("green"),
        # position="absolute",
        # left="-5px",
        position="relative",
        left="-21px",
    )

def __desktop_tablet_work_experience(model: WorkExperienceModel):
    """Deskptop and Tablet view for the Work Experience"""
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    __blip(),
                    rx.text(
                        model.worked_date, size="1", weight="medium", color=rx.color("slate", 11)
                    ),
                    align="center",
                ),
                rx.text(
                    model.position_job, size="3", weight="bold", color=rx.color("slate", 12)
                ),
                spacing="1",
            ),
            rx.text(
                model.description_job,
                font_size=TextSizes.BODY_HOME_TEXT_MOBILE.value,
            ),
            hstack_software_tags(model.software_skills),
        ),
        width="100%",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
    )

def __mobile_work_experience(model: WorkExperienceModel):
    """Mobile view for the Work Experience"""
    return rx.vstack(
        rx.text(
            model.worked_date,
            font_size=TextSizes.BODY_HOME_TEXT.value,
        ),
        rx.vstack(
            rx.box(
                rx.text(
                    model.position_job,
                    font_size=TextSizes.HEADING_H3.value,
                    weight="regular"
                ),
                rx.text(
                    model.company_and_city,
                    font_size=TextSizes.BODY_HOME_TEXT_MOBILE.value,
                ),
            ),
            rx.text(
                model.description_job,
                font_size=TextSizes.BODY_HOME_TEXT_MOBILE.value,
            ),
            hstack_software_tags(model.software_skills),
            spacing="5",
        ),
        width="100%"
    )

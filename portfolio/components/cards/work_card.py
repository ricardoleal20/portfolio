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
            __desktop_tablet_work_experience(model)
        ),
        rx.mobile_only(
            __mobile_work_experience(model)
        ),
    )


def __desktop_tablet_work_experience(model: WorkExperienceModel):
    """Desktop view for the Work Experience"""
    return rx.hstack(
        rx.text(
            model.worked_date,
            font_size=TextSizes.BODY_HOME_TEXT.value,
            width="20%"
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
            width="80%"
        )
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

"""Index page"""
import reflex as rx
# Local imports
from portfolio.pages.views.navbar import navbar
from portfolio.pages.views.welcome import welcome
from portfolio.pages.views.laboral_experience import laboral_experience
from portfolio.pages.views.education import education, certificates
from portfolio.pages.views.projects import projects
from portfolio.pages.views.open_source import open_source
from portfolio.pages.views.visa import visa_info
from portfolio.pages.views.about_me import about_me
from portfolio.pages.views.footer import footer


def index():
    """Index page"""
    return rx.box(
        navbar(),
        rx.vstack(
            rx.box(
                rx.box(
                    welcome(),
                    # width="50%",
                    margin_x="auto",
                ),
                background_size="20px 20px",
                background_image="radial-gradient(circle, hsl(0, 0%, 25%)" +
                " 1px, transparent 1px)",
                overflow="hidden",
                width="200%",  # Changed from 200% to 100%
                style={  # type: ignore
                    "overflow": "hidden",
                    "max_width": "100%",
                }
            ),
            laboral_experience(),
            rx.separator(),
            education(),
            certificates(),
            rx.separator(),
            projects(),
            open_source(),
            rx.separator(),
            visa_info(),
            rx.separator(),
            about_me(),
            # Add the video at the bottom
            rx.text(
                "Video presentation", size="6",
                margin_top="0.5em", margin_bottom="-2em"
            ),
            rx.video(
                url="/english_presentation.mov",
                light=False, controls=True,
                width="auto"
            ),
            align="center",
            justify="center",
            margin_x="8.5vw",
            spacing="9",
            margin_bottom="4em"
        ),
        footer(),
        width="100%"
    )

"""
Add the About Me view
"""
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon, paragraph_normal_and_bold

# GENERAL VARS
HEADER_TITLE = "About me"


def about_me():
    """About Me view"""
    return rx.center(
        rx.desktop_only(
            __desktop_about_me()
        ),
        rx.mobile_and_tablet(
            __mobile_about_me()
        ),
        id="about_me"
    )


def __desktop_about_me():
    """Desktop view for the About me view"""
    return rx.box(
        section_header_icon(
            "user",
            HEADER_TITLE
        ),
        rx.hstack(
            __info_about_me("75%"),
            rx.flex(
                rx.vstack(
                    rx.image(
                        src="/gato.jpeg",
                        width="auto",
                        height="250px",
                        border_radius="30px"
                    ),
                    rx.image(
                        src="/chop.jpeg",
                        width="auto",
                        height="250px",
                        border_radius="30px"
                    )
                ),
                width="25%",
                justify="center",
                align="center"
            ),
            width="100%",
            margin_top="4em",
            align="center"
        ),
        width="100%",
    )


def __mobile_about_me():
    """Mobile view for the About me view"""
    return rx.box(
        section_header_icon(
            "user",
            HEADER_TITLE
        ),
        rx.vstack(
            rx.flex(
                rx.hstack(
                rx.image(
                    src="/gato.jpeg",
                    width="auto",
                    height="200px",
                    border_radius="30px"
                ),
                    rx.image(
                    src="/chop.jpeg",
                    width="auto",
                    height="200px",
                    border_radius="30px"
                ),
                ),
                justify="center",
                align="center"
            ),
            __info_about_me(),
            width="100%",
            margin_top="4em",
            align="center",
            spacing="6"
        ),
        width="100%",
    )


def __info_about_me(width: str = "100%"):
    """Return the `About me` information"""
    return rx.vstack(
        paragraph_normal_and_bold(
            "I'm Ricardo Leal, a Mexican, dedicated and skilled ",
            ":bold:Software Engineer",
            " with a strong background in Computational Science and Applied Mathematics",
            "\n",
        ),
        paragraph_normal_and_bold(
            "I hold a ",
            ":bold:MSc. in Computational Science and Applied Mathematics",
            ", with a specialization in Computer Science, focusing on the development of APIs for"
            " industrial problem-solving. I also hold a ",
            ":bold:BSc. in Physics",
            ", where I specialized as a"
            " Computational Physicist, with a focus on Materials Science.",
        ),
        paragraph_normal_and_bold(
            "During my Bachelor, I use Python for research purposes, and learn about the correct",
            " use of the programming as a tool for research, and that give me the tools to start",
            " working as a Research Assistant on the Materials Science department, things that",
            " help me to obtain my first job as Software Engineer while I was on my last year of",
            " the university. That Job, here on ",
            ":bold:Valiot",
            " give me the expertise of how it really feels to work to solve real world problems,",
            " thing that later it would give me the inspiration to start my Master degree in ",
            " that same field.",
        ),
        paragraph_normal_and_bold(
            " I get a lot of love in programming, in automation to reduce",
            " repetitive tasks in the work and to make the implementations run faster. When I",
            " start on Valiot, I firstly start as an Implementor for",
            ":bold: ValueChainOS",
            ", using the",
            " tools that the Product team was developing to improve the implementation process,",
            " but in the first months I quickly scaled to the product team, developing different",
            " tools to reduce the workload of the implementation team, and increasing the",
            " performance of the current and existing tools.",
        ),
        paragraph_normal_and_bold(
            "I love programming, and I have a strict rule on higher quality code for everything",
            " that I do, even my personal projects or automations that I made for my home.",
            " I have a cat called ",
            ":bold:Gato",
            " that is my daily companion for my work sessions, and a dog called ",
            ":bold:Chop",
            " that is my exercise partner.",
        ),
        width=width,
    )

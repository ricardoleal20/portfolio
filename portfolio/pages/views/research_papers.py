"""
Research Papers view for the portfolio
"""
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon, main_button
from portfolio.models import ResearchPaperModel
from portfolio.styles import TextSizes, Color
# Data import
from portfolio.data import RESEARCH_PAPERS


def research_papers():
    """Research papers view"""
    return rx.box(
        section_header_icon(
            "flask-conical",
            "Research Papers"
        ),
        __body_vstack_papers(),
        id="research_papers"
    )


def __paper_card(paper: ResearchPaperModel):
    """Card component for a single research paper"""
    return rx.card(
        rx.vstack(
            # Title and year
            rx.hstack(
                rx.vstack(
                    rx.text(
                        paper.title,
                        font_size=TextSizes.HEADING_H3.value,
                        color=Color.PRIMARY.value,
                        weight="bold",
                    ),
                    rx.text(
                        " · ".join(paper.authors),
                        font_size=TextSizes.CARD_BODY.value,
                        color=rx.color("gray", 11),
                    ),
                    spacing="1",
                    align="start",
                ),
                rx.spacer(),
                rx.badge(
                    paper.year,
                    color_scheme="green",
                    variant="soft",
                    size="2",
                ),
                align="start",
                width="100%",
            ),
            # Journal
            rx.hstack(
                rx.icon("book-open", size=16, color=rx.color("gray", 11)),
                rx.text(
                    paper.journal,
                    font_size=TextSizes.CARD_BODY.value,
                    color=rx.color("gray", 11),
                    font_style="italic",
                ),
                spacing="2",
                align="center",
            ),
            # Divider
            rx.el.hr(
                background_color=Color.GREY,
                height="1px",
                width="100%",
            ),
            # Abstract
            rx.text(
                paper.abstract,
                font_size=TextSizes.CARD_BODY.value,
                text_align="justify",
            ),
            # Keywords
            rx.hstack(
                rx.text(
                    "Keywords:",
                    font_size=TextSizes.CARD_BODY.value,
                    weight="bold",
                ),
                rx.flex(
                    *[
                        rx.badge(
                            kw,
                            color_scheme="green",
                            variant="outline",
                            size="1",
                        )
                        for kw in paper.keywords
                    ],
                    wrap="wrap",
                    gap="2",
                ),
                align="center",
                flex_wrap="wrap",
                gap="2",
            ),
            # DOI and link button
            rx.hstack(
                rx.text(
                    f"DOI: {paper.doi}",
                    font_size=TextSizes.CARD_BODY.value,
                    color=rx.color("gray", 11),
                ),
                rx.spacer(),
                main_button(
                    "external-link",
                    "Read Paper",
                    paper.url,
                    "2",
                ),
                align="center",
                width="100%",
            ),
            spacing="4",
            align="start",
            padding="1em",
        ),
        width="100%",
    )


def __body_vstack_papers():
    """Body stack for research papers"""
    return rx.vstack(
        *[
            __paper_card(paper)
            for paper in RESEARCH_PAPERS
        ],
        spacing="6",
        margin_top="3em",
        width="100%",
    )

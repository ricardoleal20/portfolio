"""
Page to include a visa view.

This page will include the visa information for me, willing where I can currently work
under which conditions and if I'm willing to relocate.
"""
from dataclasses import asdict
import reflex as rx
# Local imports
from portfolio.components.miscellaneous import section_header_icon
from portfolio.data import WORK_VISA


def visa_info() -> rx.Component:
    """Give a table with my Visa Information"""
    return rx.box(
        section_header_icon(
            "compass",
            "Work Visa Eligibility"
        ),
        # Information about this section
        rx.center(
            __feature_visa_info(),
        ),
        # Table of the Visa Information
        rx.center(
            __table_visa(),
            margin_top="1.5em",
        ),
        id="visa",
        width="100%",
    )

# ======================================== #
# Create the visa highlights #
# ======================================== #


highlights = [
    {
        "title": "No Sponsor Required",
        "description": "I'm elegible to work in this countries without a sponsor."
    },
    {
        "title": "Relocation",
        "description": "I'm willing to relocate to this countries, if required."
    },
    {
        "title": "Processing Time",
        "description": "For each one of this visas, the processing time is," +
        " in average, less than 6 weeks."
    },
    {
        "title": "Required Documents",
        "description": "Almost all the required documents listed below are" +
        " available in my possession."
    }
]


def __create_highlight(title: str, description: str):
    return rx.hstack(
        rx.box(
            width="42px",
            height="42px",
            bg=rx.color("gray", 4),
            border_radius="10px",
        ),
        rx.vstack(
            rx.text(title, size="2", weight="bold"),
            rx.text(description, size="1",
                    weight="medium", color_scheme="gray"),
            spacing="1",
            width=["90%" if i <= 1 else "60%" for i in range(6)],
        ),
        width="100%",
        padding="12px 0px",
    )


def __feature_visa_info() -> rx.Component:
    """Define the Visa featured information"""
    return rx.vstack(
        # Define the info here!
        rx.text(
            "As a Mexican Citizen, I'm elegible to work in some countries" +
            " under specific conditions. Some highlights about this" +
            " visas are:",
            size="4"
        ),
        # Define the highlights here!
        rx.center(
            rx.hstack(
                *[
                    __create_highlight(item["title"], item["description"])
                    for item in highlights
                ],
                width="100%",
                display="grid",
                grid_template_columns=[
                    "repeat(1, 1fr)" if i <= 1 else "repeat(2, 1fr)" for i in range(6)
                ],
                # padding="24px 0px",
                spacing="0",
                # wrap="wrap",
            ),
        ),
        width="100%",
        # max_width="35em",
        display="flex",
        justify="center",
        align="center",
        margin_top="1em"
    )

# ======================================== #
# Add the table with the Visa Information #
# ======================================== #


VISA_DATA: list[dict[str, str]] = [asdict(v) for v in WORK_VISA]

def __table_visa() -> rx.Component:
    """Table with the Visa Information"""
    def render_row(data: dict[str, str]):

        # Add the possible link
        if data["application_link"]:
            application_link = rx.link(
                "More Info",
                href=data["application_link"],
                size="1",
                color=rx.color("blue", 11),
                weight="bold",
                underline="hover",
            )
        else:
            application_link = rx.text("N/A")


        return rx.table.row(
            # Add the virst cell of the Table, the one for the VISA NAME
            rx.table.cell(
                rx.text(data["visa_name"], size="1", weight="bold"),
                width="200px"
            ),
            # Add the second cell of the Table, the one for the COUNTRY
            rx.table.cell(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            data["country"],
                            size="1",
                            color=rx.color("slate", 12),
                            weight="bold",
                        ),
                        spacing="0",
                    ),
                    align="center",
                )
            ),
            # Now, include a cell for the DESCRIPTION
            rx.table.cell(
                rx.text(
                    data["description"],
                    size="1",
                    weight="medium"
                ),
                width="320px",
                max_width="320px",
                white_space="normal",
                word_wrap="break-word"
            ),
            # Include a cell for the ELEGIBILITY CONDITIONS
            rx.table.cell(
                rx.list.unordered(  # pylint: disable=E1101 # type: ignore
                    rx.foreach(
                        data["required_documents"],
                        rx.list_item
                    ),
                    align_items="start",
                    spacing="2",
                )
            ),
            # Include a cell for the LINK
            rx.table.cell(application_link),
            white_space="nowrap",
            align="center",
        )

    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    [
                        "Visa Name", "Country",
                        "Description", "Requirements",
                        "Link"
                    ],
                    lambda title: rx.table.column_header_cell(
                        rx.text(
                            title, size="1", weight="bold", color=rx.color("slate", 11)
                        )
                    ),
                ),
                white_space="nowrap",
            ),
        ),
        rx.table.body(*[render_row(d) for d in VISA_DATA]),
        width="100%",
        variant="ghost",
        max_width="800px",
        size="2",
    )

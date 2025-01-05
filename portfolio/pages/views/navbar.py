"""
Navigation Bar view
"""
import reflex as rx
# Local imports
from portfolio.styles import heading_navbar, border_spacer
from portfolio import __info__ as info
from portfolio.components.miscellaneous import navbar_link, navbar_menu_item_link


def navbar():
    """Navigation Bar for the project"""
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.link(
                    rx.heading(
                        info.USERNAME,
                        style=heading_navbar,  # type: ignore
                        as_="h3"
                    ),
                    href="/"
                ),
                rx.hstack(
                    navbar_link("Experience", "experience"),
                    navbar_link("Education", "education"),
                    navbar_link("Projects", "projects"),
                    navbar_link("Open Source", "open_source"),
                    navbar_link("Work Visa Eligibility", "visa"),
                    navbar_link("About me", "about_me"),
                    rx.color_mode.button(),
                    justify="end",
                    spacing="5",
                    align="center"
                ),
                align_items="center",
                justify="between",
                padding_x="3em",
                padding_y="1em"
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.link(
                    rx.heading(
                        info.USERNAME,
                        style=heading_navbar,  # type: ignore
                        as_="h3"
                    ),
                    href="/"
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        navbar_menu_item_link("Experience", "experience"),
                        navbar_menu_item_link("Education", "education"),
                        navbar_menu_item_link("Projects", "projects"),
                        navbar_menu_item_link("Open source", "open_source"),
                        navbar_menu_item_link("Work Visa Eligibility", "visa"),
                        navbar_menu_item_link("About me", "about_me"),
                    ),
                    justify="end"
                ),
                align_items="center",
                justify="between",
            ),
            padding_y="2em",
            padding_x="3em",
        ),
        border_bottom=border_spacer,
        position="sticky",
        top="0px",
        z_index="999",
        width="100%",
        background_color=rx.color_mode_cond(light="white", dark="#111113")
    )

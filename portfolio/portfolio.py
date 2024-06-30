"""
Index for my FrontEnd application
"""
import reflex as rx
# Local imports
from portfolio.pages import index

# ========================================== #
#                    APP                     #
# ========================================== #

app = rx.App(  # pylint: disable=E1102
    theme=rx.theme(
        appearance="dark"
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap",
    ],
    style={
        "font_family": "Montserrat, sans-serif",
        "font_size": "13px"
    }
)
app.add_page(index, title="Portfolio :: Ricardo Leal")

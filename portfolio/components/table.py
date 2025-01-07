"""
Create a Table component that can use different models and their equivalent fields
to show information.

This is thinking in a way to create a component to show the Open Source projects and
the projects that I have worked on.
"""
import reflex as rx


def create_table_component(
    component_info: list[dict[str, list | dict | rx.Component | str]],
    **custom_config
) -> rx.Component:
    """Create the table component to show information"""

    if "width" not in custom_config:
        custom_config["width"] = "100%"
    if "variant" not in custom_config:
        custom_config["variant"] = "surface"
    if "max_width" not in custom_config:
        custom_config["max_width"] = "800px"
    if "size" not in custom_config:
        custom_config["size"] = "2"

    return rx.table.root(
        # Define the header
        rx.table.header(
            rx.table.row(*[
                rx.table.column_header_cell(
                    rx.text(title, font_size="12px", weight="bold"),
                    align="center",
                ) for title in component_info[0].keys()
            ]),
            align="center",
        ),
        # Define the body
        rx.table.body(*[
            __create_field_info(data)
            for data in component_info
        ]),
        # Extra configuration
        **custom_config
    )


def __create_field_info(
    data: dict[str, list | dict | rx.Component | str]
) -> rx.Component:
    """Based on the parameter given, return an implementation of the row"""
    # Depending on the data, define the row
    # For each key in the data, create a cell
    cells: list[rx.Component] = []
    for entry in data.values():
        # IF the value is a list of things, create a list of items
        if isinstance(entry, (list, tuple, set)):
            cells.append(
                rx.table.cell(
                    # *[rx.text(item, font_size="12px") for item in entry],
                    rx.list.unordered(  # pylint: disable=E1101 # type: ignore
                        *[rx.list_item(item) for item in entry],
                        align_items="start",
                        spacing="2",
                    )
                )
            )
        # If it is a dict, then it should include extra information for the cell
        elif isinstance(entry, dict):
            if not "value" in entry:
                raise ValueError(
                    "The `value` key is required in the dictionary")
            # Get the value
            inner_value = entry.get("value")
            extra_info: dict = {k: v for k, v in entry.items() if k != "value"}
            # Create the cell with this information
            cells.append(
                rx.table.cell(
                    inner_value,
                    **extra_info,
                )
            )
        # IF the value is a string, just create the cell
        elif isinstance(entry, str):
            cells.append(
                rx.table.cell(
                    rx.text(entry, font_size="12px"),
                )
            )
        # If is something else...
        else:
            cells.append(rx.table.cell(entry))
    # Return the row at the very end
    return rx.table.row(
        *cells,
        align="center",
        white_space="nowrap",
    )

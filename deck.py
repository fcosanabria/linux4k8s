#!/usr/bin/env python

import inspect
import shutil  # For terminal size detection
from textwrap import dedent
from pathlib import Path

from rich.align import Align
from rich.console import Group, RenderableType
from rich.layout import Layout
from rich.markdown import Markdown
from rich.padding import Padding
from rich.style import Style
from rich.text import Text

from spiel import Slide, SuspendType, Triggers, present
from spiel.deck import Deck

# ===== Configuration =====
# Colors for Markdown headings
H1_COLOR = "bright_cyan"
H2_COLOR = "bright_green"
H3_COLOR = "bright_yellow"

# ===== Create the deck =====
deck = Deck(name="Linux para contenerización y Kubernetes")


# ===== Utility functions =====
def get_terminal_size():
    """Get the current terminal size."""
    return shutil.get_terminal_size()


def styled_markdown(text: str) -> Markdown:
    """Create styled Markdown with custom heading colors."""
    md = Markdown(
        dedent(text),
        justify="center",
        code_theme="monokai",
        hyperlinks=True,
    )

    # Style headings by overriding the default styles
    md.heading_styles = {
        1: Style(color=H1_COLOR, bold=True),
        2: Style(color=H2_COLOR, bold=True),
        3: Style(color=H3_COLOR, bold=True),
    }

    return md


def format_content(content: RenderableType, title: str = None, current: int = None,
                   total: int = None) -> RenderableType:
    """Format content with padding and add trigger counter footer if provided."""
    padded_content = Padding(content, pad=(1, 2, 1, 2))

    # If we have trigger information, add it as a footer
    if current is not None and total is not None:
        # Create a footer with the trigger counter
        counter_text = Text(f"Progress: {current}/{total}", style=Style(color="grey74", dim=True))
        footer = Align.right(counter_text)

        # Combine content and footer
        return Group(
            padded_content,
            footer
        )
    else:
        return padded_content


# ===== Slides =====

@deck.slide(title="Bienvenidos")
def title_slide() -> RenderableType:
    """Cover slide for the presentation title."""
    title_text = Text("Linux para contenerización y Kubernetes", style=Style(color="bright_magenta", bold=True))
    subtitle_text = Text("Pre-taller para Kubernetes", style=Style(color="bright_white"))
    date_text = Text("Abril 21, 2025", style=Style(color="grey74"))
    author_text = Text("Francisco Sanabria", style=Style(color="grey74"))

    content = Group(
        Align.center(title_text),
        Align.center(subtitle_text),
        Align.center(Text("")),  # Spacer
        Align.center(date_text),
        Align.center(author_text),
    )

    return format_content(content)


@deck.slide(title="Contacto")
def contact_slide(triggers: Triggers) -> RenderableType:
    """Contact slide with gradual reveal of contact information."""
    title = Align.center(
        Text("Francisco Sanabria", style=Style(color="bright_cyan", bold=True)),
    )

    # Define contact items that will be revealed one by one
    contacts = [
        Text.from_markup("[bright_magenta]Site Reliability Engineer[/bright_magenta] @ [orange3]Datasite[/orange3] | [blue3]Certified Kubernetes Administrator[/blue3] | 10 years of experience in IT"),
        Text("Homelab & Music Nerd | Visual Artist"),
        Text.from_markup("[bright_blue]Email:[/bright_blue] [link=mailto:fco.sanabria@tuta.io]fco.sanabria@tuta.io[/link]"),
        # Text.from_markup("[bright_blue]Website:[/bright_blue] [link=https://example.com]example.com[/link]"),
        Text.from_markup(
            "[bright_blue]GitHub:[/bright_blue] [link=https://github.com/fcosanabria]github.com/fcosanabria[/link]"),
        # Text.from_markup("[bright_blue]Twitter:[/bright_blue] [link=https://twitter.com/username]@username[/link]"),
        Text.from_markup(
            "[bright_blue]LinkedIn:[/bright_blue] [link=https://linkedin.com/in/fcosanabria]linkedin.com/in/fcosanabria[/link]"),
    ]

    # Show only the items that have been triggered
    visible_contacts = [
        Padding(contact, pad=(0, 0, 1, 1))
        for i, contact in enumerate(contacts)
        if i < len(triggers)
    ]

    # Combine all visible elements
    content = Group(
        title,
        Padding(Text(""), pad=(1, 0)),  # Spacer
        *visible_contacts,
    )

    return format_content(content, current=len(triggers), total=len(contacts))

@deck.slide(title="Agenda")
def markdown_slide(triggers: Triggers) -> RenderableType:
    # Base markdown content with multiple sections
    markdown_sections = [
        """
        # Agenda

        Estos son los temas que vamos a ver el día de hoy:
        """,

        """
        ## Second Point

        1. Numbered item one
        2. Numbered item two
        3. Numbered item three
        """,

        """
        ### Pausa
        
        Vamos a tener una pausa de 12 minutos.
        """,
    ]

    # Show only the sections that have been triggered
    visible_sections = markdown_sections[:min(len(triggers), len(markdown_sections))]
    combined_markdown = "\n".join(visible_sections)

    # Instructions text at the bottom if not all sections shown
    content = styled_markdown(combined_markdown)

    if len(triggers) < len(markdown_sections):

        content = Group(content)

    return format_content(content, current=len(triggers), total=len(markdown_sections))

@deck.slide(title="Linux Namespaces")
def markdown_slide(triggers: Triggers) -> RenderableType:
    markdown_sections = [
        """
        # Linux Namespaces

        También llamados espacios de nombre en Linux.
        """,

        """
        ## First Point

        * This is the first bullet point
        * With some important details
        * And key considerations
        """,

        """
        ## Second Point

        1. Numbered item one
        2. Numbered item two
        3. Numbered item three
        """,

        """
        ### Additional Details

        ```python
        def example_code():
            print("This is some example code")
            return True
        ```
        """,
    ]

    # Show only the sections that have been triggered
    visible_sections = markdown_sections[:min(len(triggers), len(markdown_sections))]
    combined_markdown = "\n".join(visible_sections)

    # Instructions text at the bottom if not all sections shown
    content = styled_markdown(combined_markdown)

    if len(triggers) < len(markdown_sections):

        content = Group(content)

    return format_content(content, current=len(triggers), total=len(markdown_sections))



@deck.slide(title="Template for Markdown")
def markdown_slide(triggers: Triggers) -> RenderableType:
    # Base markdown content with multiple sections
    markdown_sections = [
        """
        # Template for Markdown

        This is the introduction to the main topic.
        """,

        """
        ## First Point

        * This is the first bullet point
        * With some important details
        * And key considerations
        """,

        """
        ## Second Point

        1. Numbered item one
        2. Numbered item two
        3. Numbered item three
        """,

        """
        ### Additional Details

        ```python
        def example_code():
            print("This is some example code")
            return True
        ```
        """,
    ]

    # Show only the sections that have been triggered
    visible_sections = markdown_sections[:min(len(triggers), len(markdown_sections))]
    combined_markdown = "\n".join(visible_sections)

    # Instructions text at the bottom if not all sections shown
    content = styled_markdown(combined_markdown)

    if len(triggers) < len(markdown_sections):

        content = Group(content)

    return format_content(content, current=len(triggers), total=len(markdown_sections))


@deck.slide(title="Two Column Slide")
def two_column_slide(triggers: Triggers) -> RenderableType:
    """Generic two-column markdown slide."""
    # Left column content
    left_markdown = """
    # Left Column

    ## Points

    * First important point
    * Second important point
    * Third important point

    ### Details

    Some additional details that provide more context.
    """

    # Right column content with trigger-based reveal
    right_markdown_sections = [
        """
        # Right Column

        Initial content in the right column.
        """,

        """
        ## Supporting Evidence

        1. First piece of evidence
        2. Second piece of evidence
        """,

        """
        ### Conclusion

        The final takeaway or conclusion for this slide.
        """
    ]

    # Show only the right sections that have been triggered
    visible_right_sections = right_markdown_sections[:min(len(triggers), len(right_markdown_sections))]
    combined_right_markdown = "\n".join(visible_right_sections)

    # Create the layout
    root = Layout()
    root.split_row(
        Layout(styled_markdown(left_markdown), name="left", ratio=1),
        Layout(styled_markdown(combined_right_markdown), name="right", ratio=1),
    )

    # Add instructions if not all sections revealed
    if len(triggers) < len(right_markdown_sections):
        instructions = Text("Press 't' to reveal more content", style=Style(dim=True))
        content = Group(
            root,
            Align.center(instructions),
        )
    else:
        content = root

    return format_content(content, current=len(triggers), total=len(right_markdown_sections))


# ===== Extra helper slides you might need =====

@deck.slide(title="Image Slide")
def image_slide() -> RenderableType:
    """Example slide with an image (if needed)."""
    from spiel.renderables.image import Image

    # Replace it with your actual image path
    image_path = Path("./path/to/your/image.jpg")

    title = Align.center(
        Text("Image Example", style=Style(color="bright_cyan", bold=True))
    )

    # If the image exists, display it
    if image_path.exists():
        image = Image.from_file(image_path)
        content = Group(
            title,
            Padding(Text(""), pad=(1, 0)),  # Spacer
            Align.center(image),
        )
    else:
        # Placeholder if the image doesn't exist
        content = Group(
            title,
            Padding(Text(""), pad=(1, 0)),  # Spacer
            Align.center(Text(f"[Image would be displayed here: {image_path}]", style=Style(dim=True))),
        )

    return format_content(content)


@deck.slide(title="Code Slide")
def code_slide() -> RenderableType:
    """Example slide with code (if needed)."""
    from rich.syntax import Syntax

    title = Align.center(
        Text("Code Example", style=Style(color="bright_cyan", bold=True))
    )

    # Example Python code
    code = """
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    # Calculate the first 10 Fibonacci numbers
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    """

    syntax = Syntax(
        dedent(code),
        lexer="python",
        theme="monokai",
        line_numbers=True,
        word_wrap=True,
    )

    content = Group(
        title,
        Padding(Text(""), pad=(1, 0)),  # Spacer
        syntax,
    )

    return format_content(content)


# ===== Custom key bindings =====
# Example of a custom key binding to edit the presentation file
def edit_this_file(suspend: SuspendType) -> None:
    """Open this file in the default editor."""
    from click import edit
    with suspend():
        edit(filename=__file__)

# ===== Main function =====
if __name__ == "__main__":
    present(__file__)

# import inspect
# from textwrap import dedent
#
# from rich.box import SQUARE
# from rich.console import RenderableType, Group
# from rich.layout import Layout
# from rich.markdown import Markdown
# from rich.padding import Padding
# from rich.panel import Panel
# from rich.style import Style
# from rich.syntax import Syntax
# from rich.align import Align
# from rich.text import Text
#
# from spiel import Deck, Slide, present, Triggers
# from spiel.demo.demo import pad_markdown
#
# deck = Deck(name="Linux para contenerización y Kubernetes")
#
# @deck.slide(title="Datasite")
# def slide_1() -> RenderableType:
#     content = pad_markdown(
#     f"""\
#     # Linux para contenerización y Kubernetes: Pre-taller para Kubernetes
#     """
#     )
#     return Align(content, vertical="middle")
#
# @deck.slide(title="Introducción")
# def slide_2(triggers: Triggers) -> RenderableType:
#     content = [
#         Text.from_markup(
#             f""" # Linux para contenerización y Kubernetes"""
#         ),
#         Text("Francisco Sanabria") if len(triggers) >= 1 else None,
#         Text("Site Reliability Engineer @ Datasite | Certified Kubernetes Administrator | 10 years experience in IT")if len(triggers) >= 2 else None,
#         Text("Homelab & Music Nerd | Visual Artist") if len(triggers) >= 3 else None,
#     ]
#
#     return Group(
#         *(Padding(Align.center(line), pad=(0, 0, 1, 0)) for line in content if line is not None)
#     )
#
# @deck.slide(title="Revealing Content")
# def reveal(triggers: Triggers) -> RenderableType:
#     lines = [
#         Text.from_markup(
#             f"This slide has been triggered [yellow]{len(triggers)}[/yellow] time{'s' if len(triggers) > 1 else ''}."
#         ),
#         Text("First line.", style=Style(color="red")) if len(triggers) >= 1 else None,
#         Text("Second line.", style=Style(color="blue")) if len(triggers) >= 2 else None,
#         Text("Third line.", style=Style(color="green")) if len(triggers) >= 3 else None,
#     ]
#
#     return Group(
#         *(Padding(Align.center(line), pad=(0, 0, 1, 0)) for line in lines if line is not None)
#     )
#
# @deck.slide(title="Slide Title")
# def slide_content() -> RenderableType:
#     return Align(
#         Text.from_markup(
#             "[blue]Your[/blue] [red underline]content[/red underline] [green italic]here[/green italic]!"
#         ),
#         align="center",
#         vertical="middle",
#     )
#
# if __name__ == "__main__":
#     present(__file__)
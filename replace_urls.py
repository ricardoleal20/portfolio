"""
File in Python that include a function that replace all the URLs by a pre-determined url
"""
import os
import re

patterns = [r'/gato.jpeg', r'/profile.png', r'/favicon.ico', r'/_next/static/']


def replace_patterns(url: str) -> None:
    """Replace the patterns in the URL"""
    # Read the index.html file
    with open('./index.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Modificar el contenido del archivo HTML
    for pattern in patterns:
        content = re.sub(pattern, f'{url}{pattern}', content)

    # Guardar el contenido modificado en un nuevo archivo HTML
    with open('./index.html', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == "__main__":
    replace_patterns(
        os.environ.get("URL", "")
    )

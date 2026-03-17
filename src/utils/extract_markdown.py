import re

RE_IMAGES = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
RE_LINKS = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(RE_IMAGES, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(RE_LINKS, text)


if __name__ == "__main__":
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    extract_markdown_images(text)

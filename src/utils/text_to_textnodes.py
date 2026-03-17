from utils.split_images_and_links import split_nodes_link, split_nodes_image
from utils.split_nodes_delimiter import split_nodes_delimiter
from nodes.textnode import TextNode, TextType


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    images = split_nodes_image(code)
    links = split_nodes_link(images)
    return links

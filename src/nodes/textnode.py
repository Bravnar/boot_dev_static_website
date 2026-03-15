from enum import Enum

from nodes.leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


def text_node_to_html_node(text_node):
    text = text_node.text
    text_type = text_node.text_type
    match text_type:
        case text_type.TEXT:
            return LeafNode(None, value=text)
        case text_type.BOLD:
            return LeafNode("b", value=text)
        case text_type.ITALIC:
            return LeafNode("i", value=text)
        case text_type.CODE:
            return LeafNode("code", value=text)
        case text_type.LINK:
            return LeafNode("a", value=text, props={"href": text_node.url})
        case text_type.IMAGE:
            return LeafNode("img", "", props={"src": text_node.url, "alt": text})
        case _:
            raise Exception("Invalid text type")


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text_true = self.text == other.text
        text_type_true = self.text_type == other.text_type
        url_true = self.url == other.url
        if text_true and text_type_true and url_true:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"

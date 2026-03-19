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
    # print(f"text: {repr(text)}, type: {text_type}")
    match text_type:
        case TextType.TEXT:
            return LeafNode(None, value=text)
        case TextType.BOLD:
            return LeafNode("b", value=text)
        case TextType.ITALIC:
            return LeafNode("i", value=text)
        case TextType.CODE:
            return LeafNode("code", value=text)
        case TextType.LINK:
            return LeafNode("a", value=text, props={"href": text_node.url})
        case TextType.IMAGE:
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
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

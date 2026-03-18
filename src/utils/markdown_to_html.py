from nodes.textnode import TextNode, TextType, text_node_to_html_node
from nodes.parentnode import ParentNode

from utils.block_to_block_type import block_to_block_type, BlockType
from utils.markdown_to_blocks import markdown_to_blocks
from utils.text_to_textnodes import text_to_textnodes


def text_to_children(text):
    clean_text = text.replace("\n", " ")
    text_nodes = text_to_textnodes(clean_text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))
    return leaf_nodes


def create_heading(block):
    heading_level = len(block) - len(block.lstrip("#"))
    leaf_nodes = text_to_children(block.lstrip("#").lstrip())
    header_node = ParentNode(f"h{heading_level}", leaf_nodes)
    return header_node


def create_code(block):
    clean_block = block.lstrip("```\n").strip("```")
    text_node = TextNode(clean_block, TextType.CODE)
    leaf_node = text_node_to_html_node(text_node)
    code_node = ParentNode("pre", [leaf_node])
    return code_node


def create_quote(block):
    lines = block.split("\n")
    clean_lines = [x.strip(">").strip() for x in lines]
    leaf_nodes = text_to_children(" ".join(clean_lines))
    quote_node = ParentNode("blockquote", leaf_nodes)
    return quote_node


def create_paragraph(block):
    leaf_nodes = text_to_children(block)
    paragraph_node = ParentNode("p", leaf_nodes)
    return paragraph_node


def create_ul(block):
    lines = block.split("\n")
    clean_lines = [x.strip("- ") for x in lines]
    list_nodes = []
    for line in clean_lines:
        leaf_nodes = text_to_children(line)
        new_node = ParentNode("li", leaf_nodes)
        list_nodes.append(new_node)
    ul_node = ParentNode("ul", list_nodes)
    return ul_node


def create_ol(block):
    lines = block.split("\n")
    clean_lines = [x.split(". ", 1)[1] for x in lines]
    list_nodes = []
    for line in clean_lines:
        leaf_nodes = text_to_children(line)
        new_node = ParentNode("li", leaf_nodes)
        list_nodes.append(new_node)
    ol_node = ParentNode("ol", list_nodes)
    return ol_node


def create_block_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return create_heading(block)
        case BlockType.CODE:
            return create_code(block)
        case BlockType.QUOTE:
            return create_quote(block)
        case BlockType.UL:
            return create_ul(block)
        case BlockType.OL:
            return create_ol(block)
        case BlockType.PARAGRAPH:
            return create_paragraph(block)


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    list_of_parents = []
    for block in blocks:
        node = create_block_node(block)
        list_of_parents.append(node)
    return ParentNode("div", list_of_parents)

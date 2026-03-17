from nodes.textnode import TextNode, TextType
from utils.extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        node_text = node.text
        start, rest = None, None
        for image in images:
            (alt, link) = image
            start, rest = node_text.split(f"![{alt}]({link})", 1)
            if start:
                new_nodes.append(TextNode(start, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
            node_text = rest
        if rest:
            new_nodes.append(TextNode(rest, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        node_text = node.text
        start, rest = None, None
        for link in links:
            (text, url) = link
            start, rest = node_text.split(f"[{text}]({url})", 1)
            if start:
                new_nodes.append(TextNode(start, TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            node_text = rest
        if rest:
            new_nodes.append(TextNode(rest, TextType.TEXT))
    return new_nodes

from nodes.textnode import TextNode, TextType


def split_text_by_delimiter(
    text: str,
    delimiter: str,
    text_type: TextType,
):
    if not text:
        return []
    if delimiter not in text:
        return [TextNode(text, TextType.TEXT)]

    current_nodes = []
    start = text.find(delimiter) + len(delimiter)
    end = text.find(delimiter, start)
    # print("Start:", start)
    if start != len(delimiter):
        current_nodes.append(TextNode(text[: start - len(delimiter)], TextType.TEXT))
    # print("End:", end)
    current_nodes.append(TextNode(text[start:end], text_type))
    remaining_text = text[end + len(delimiter) :]
    return current_nodes + split_text_by_delimiter(remaining_text, delimiter, text_type)


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        delim_count = node.text.count(delimiter)
        if node.text_type != TextType.TEXT or delim_count == 0:
            new_nodes.append(node)
            continue
        # print(f"Delimiter count: {delim_count}")
        if delim_count % 2:
            raise Exception("Invalid syntax in markdown text")
        else:
            list_of_nodes = split_text_by_delimiter(node.text, delimiter, text_type)
            new_nodes.extend(list_of_nodes)
    return new_nodes


if __name__ == "__main__":
    print("Hello from split_nodes_delimiter function")
    node = TextNode(
        "Hello **World**! All the **people** in it! and the rest of **assholes**",
        TextType.TEXT,
    )

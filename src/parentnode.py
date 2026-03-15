from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("not html tag provided")
        if not self.children:
            raise ValueError("parent node must have children")
        html_string = [f"<{self.tag}{self.props_to_html()}>"]
        for child in self.children:
            html_string.append(child.to_html())
        html_string.append(f"</{self.tag}>")
        return "".join(html_string)


if __name__ == "__main__":
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ],
        {"test": "this_is_a_test_prop"},
    )

    print(node.to_html())

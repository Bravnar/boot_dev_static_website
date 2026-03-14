class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_line = ""
        if self.props is None:
            return html_line
        for prop in self.props.keys():
            html_line += f" {prop}={self.props[prop]}"
        return html_line

    def __repr__(self) -> str:
        msg = []
        msg.append("HTMLNode:")
        msg.append(f"Tag: {self.tag}")
        msg.append(f"Value: {self.value}")
        msg.append("Children:")
        if self.children is None:
            msg.append("\tEmpty")
        else:
            for child in self.children:
                msg.append(f"\t{child}")
        msg.append("Props:")
        if self.props is None:
            msg.append("\tEmpty")
        else:
            for prop in self.props:
                msg.append(f"\t{prop}: {self.props[prop]}")
        return "\n".join(msg)


if __name__ == "__main__":
    html_node = HTMLNode(
        "<p>",
        "Hello World!",
        ["child1", "child2", "child3"],
        {"href": "https://google.com", "target": "_blank"},
    )
    print(html_node)
    print(html_node.props_to_html())

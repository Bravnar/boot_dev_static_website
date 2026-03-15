from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return str(self.value)
        prop_string = self.props_to_html()
        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        msg = []
        msg.append("LeafNode:")
        msg.append(f"Tag: {self.tag}")
        msg.append(f"Value: {self.value}")
        msg.append("Props:")
        if self.props is None:
            msg.append("\tEmpty")
        else:
            for prop in self.props:
                msg.append(f"\t{prop}: {self.props[prop]}")
        return "\n".join(msg)

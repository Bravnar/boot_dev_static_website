import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("a", "Click Me!", {"href": "https://google.com"}),
            LeafNode("p", "The Link above will take you to Google!"),
            LeafNode("h1", "Random Title Bro!"),
        ]
        parent_node = ParentNode("div", children, {"style": "color_or_whatever"})
        expected = '<div style="color_or_whatever"><a href="https://google.com">Click Me!</a><p>The Link above will take you to Google!</p><h1>Random Title Bro!</h1></div>'
        self.assertEqual(parent_node.to_html(), expected)

    def test_value_err_no_childre(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()

    def test_value_err_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("p", "Hello World!")])
            node.to_html()

    def test_to_html_with_empty_children_list(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "div",
            [ParentNode("span", [ParentNode("b", [LeafNode(None, "Deep text")])])],
        )
        expected = "<div><span><b>Deep text</b></span></div>"
        self.assertEqual(node.to_html(), expected)

    def test_mixed_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                ParentNode("span", [LeafNode("i", "italic")]),
                LeafNode(None, "plain"),
            ],
        )
        expected = "<p><b>Bold</b><span><i>italic</i></span>plain</p>"
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()

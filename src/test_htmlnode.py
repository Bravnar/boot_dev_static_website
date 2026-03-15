import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_empty(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_values(self):
        node = HTMLNode("test_tag", "test_value")
        self.assertEqual(node.tag, "test_tag")
        self.assertEqual(node.value, "test_value")

    def test_props_to_html_formatting(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()

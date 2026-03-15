import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a", "Click Me!", {"href": "https://google.com", "target": "_blank"}
        )
        expected = '<a href="https://google.com" target="_blank">Click Me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            print(node.to_html())

    def test_no_tag(self):
        node = LeafNode("", "plaintext")
        self.assertEqual(node.tag, None)

    if __name__ == "__main__":
        unittest.main()

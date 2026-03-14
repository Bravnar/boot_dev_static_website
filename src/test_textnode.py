import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_simple(self):
        node = TextNode("potato", TextType.ITALIC)
        node2 = TextNode("potato", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("potato", TextType.LINK, "https://boot.dev")
        node2 = TextNode("potato", TextType.LINK, "https://boot.com")
        self.assertNotEqual(node, node2)

    def test_not_equal_edge(self):
        node = TextNode("potato", TextType.LINK, "https://boot.dev")
        node2 = TextNode("potato", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

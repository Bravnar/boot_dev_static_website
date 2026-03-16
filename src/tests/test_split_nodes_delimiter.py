import unittest

from utils.split_nodes_delimiter import split_nodes_delimiter
from nodes.textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        nodes = [TextNode("This text is **bold**", TextType.TEXT)]
        expected = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_italic(self):
        nodes = [TextNode("This text is _italic_", TextType.TEXT)]
        expected = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "_", TextType.ITALIC), expected)

    def test_code(self):
        nodes = [TextNode("This text is `code`", TextType.TEXT)]
        expected = [
            TextNode("This text is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "`", TextType.CODE), expected)

    def test_beginning_of_sentence_delim(self):
        nodes = [TextNode("**Beginning of sentence** bold", TextType.TEXT)]
        expected = [
            TextNode("Beginning of sentence", TextType.BOLD),
            TextNode(" bold", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("This phrase has **one** word that is bold", TextType.TEXT),
            TextNode(
                "This **one** here has **two** words that are bold", TextType.TEXT
            ),
            TextNode(
                "This **one** here has **three** words that are **bold**", TextType.TEXT
            ),
        ]
        expected = [
            TextNode("This phrase has ", TextType.TEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" word that is bold", TextType.TEXT),
            TextNode("This ", TextType.TEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" here has ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" words that are bold", TextType.TEXT),
            TextNode("This ", TextType.TEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" here has ", TextType.TEXT),
            TextNode("three", TextType.BOLD),
            TextNode(" words that are ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected)

    def test_unclosed_delimiter(self):
        nodes = [TextNode("I forgot to close the **delimiter", TextType.TEXT)]

        with self.assertRaises(Exception):
            print(split_nodes_delimiter(nodes, "**", TextType.BOLD))

    def test_skipping_preformatted(self):
        nodes = [
            TextNode("Hi I am _already_ italic", TextType.ITALIC),
            TextNode("_italic_ me daddy", TextType.TEXT),
        ]
        expected = [
            TextNode("Hi I am _already_ italic", TextType.ITALIC),
            TextNode("italic", TextType.ITALIC),
            TextNode(" me daddy", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "_", TextType.ITALIC), expected)

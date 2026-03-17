import unittest

from utils.split_images_and_links import split_nodes_image, split_nodes_link
from nodes.textnode import TextNode, TextType


class TestSplitImagesAndLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [url_to_youtube](https://youtube.com) and another [url_to_google](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("url_to_youtube", TextType.LINK, "https://youtube.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("url_to_google", TextType.LINK, "https://google.com"),
            ],
            new_nodes,
        )

    def test_split_empty(self):
        new_nodes = split_nodes_link([])
        self.assertEqual([], new_nodes)

    def test_split_only_link(self):
        nodes = [
            TextNode("[url_to_youtube](https://youtube.com)", TextType.TEXT),
            TextNode(
                "[url_to_google](https://google.com) <- this here is google",
                TextType.TEXT,
            ),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("url_to_youtube", TextType.LINK, "https://youtube.com"),
                TextNode("url_to_google", TextType.LINK, "https://google.com"),
                TextNode(" <- this here is google", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()

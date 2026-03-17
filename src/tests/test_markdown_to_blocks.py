import unittest
from utils.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_more(self):
        md = """






# This is an h1 header



## This is an h2 header






### This is an h3 header



This is another paragraph with a \n random new line in there and extra spaces
This is the continued paragraph should be in the same block



This is an image ![img](https://random.image)



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is an h1 header",
                "## This is an h2 header",
                "### This is an h3 header",
                "This is another paragraph with a \n random new line in there and extra spaces\nThis is the continued paragraph should be in the same block",
                "This is an image ![img](https://random.image)",
            ],
        )

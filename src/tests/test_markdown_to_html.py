import unittest
from utils.markdown_to_html import markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quotes(self):
        md = """
# Hello World!

> Great minds think alike
>
> Said no one ever

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Hello World!</h1><blockquote>Great minds think alike  Said no one ever</blockquote></div>",
        )

    def test_ul_ol(self):
        md = """
- hello
- world
- !

1. Hello
2. Dev
3. Not so bad

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>hello</li><li>world</li><li>!</li></ul><ol><li>Hello</li><li>Dev</li><li>Not so bad</li></ol></div>",
        )

    def test_bigger_ol(self):
        md = """
10. yo
111. bro
1111. hows stuff
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>10. yo 111. bro 1111. hows stuff</p></div>")

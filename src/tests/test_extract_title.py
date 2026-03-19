import unittest

from utils.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        md = """
# This is my title

Random Paragraph
"""
        title = extract_title(md)
        self.assertEqual(title, "This is my title")

    def test_multiple_title(self):
        md = """
This is random intro text

## This is not a title

# This is a title

```
some_code that involves a header for the luls
# yo
```

# And another title not to be extracted
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")


if __name__ == "__main__":
    unittest.main()

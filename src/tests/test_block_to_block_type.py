import unittest

from utils.block_to_block_type import BlockType, block_to_block_type
from utils.markdown_to_blocks import markdown_to_blocks


class TestBlockToBlockType(unittest.TestCase):
    def test_md_to_block_type(self):
        md = """
# This is a title

- I like to announce that this is a test
- That I wrote
- Myself

```
void ft_putstr(char *str) {
    while(str) {
        write(1, str++, 1);
    }
}
```

1. I rock
2. and roll
3. baby

> Do you like dags?
> Dags?
> Ya dags
> Oooh, dogs. Yeah I like dags, I like caravans more.

####### Not a title

>quote

>quote
not a quote

1. list
not a list

- list
not a list

1.not a list

```
not a code

Simple paragraph line with **bold** text inside
"""
        blocks = markdown_to_blocks(md)
        block_types = [block_to_block_type(x) for x in blocks]
        self.assertListEqual(
            [
                BlockType.HEADING,
                BlockType.UL,
                BlockType.CODE,
                BlockType.OL,
                BlockType.QUOTE,
                BlockType.PARAGRAPH,
                BlockType.QUOTE,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
            block_types,
        )

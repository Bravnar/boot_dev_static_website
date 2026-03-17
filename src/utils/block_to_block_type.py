from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered list"
    OL = "ordered list"


def check_heading(lines):
    pattern = r"^(#{1,6} )"
    for line in lines:
        if not re.findall(pattern, line):
            return BlockType.PARAGRAPH
    return BlockType.HEADING


def check_code(lines):
    if lines[0] == "```" and lines[-1].endswith("```"):
        return BlockType.CODE
    return BlockType.PARAGRAPH


def check_quote(lines):
    for line in lines:
        if not ((line[0] == ">" and line[1] != " ") or line.startswith("> ")):
            return BlockType.PARAGRAPH
    return BlockType.QUOTE


def check_ul(lines):
    for line in lines:
        if not line.startswith("- "):
            return BlockType.PARAGRAPH
    return BlockType.UL


def check_ol(lines):
    for line in lines:
        if not re.findall(r"^(\d+. )", line):
            return BlockType.PARAGRAPH
    return BlockType.OL


def block_to_block_type(block):
    block_by_line = block.strip().split("\n")  # temporary strip
    first_line = block_by_line[0]
    if first_line.startswith("#"):
        return check_heading(block_by_line)
    if first_line.startswith("```"):
        return check_code(block_by_line)
    if first_line.startswith(">"):
        return check_quote(block_by_line)
    if first_line.startswith("- "):
        return check_ul(block_by_line)
    if first_line[0].isdigit():
        return check_ol(block_by_line)
    return BlockType.PARAGRAPH


if __name__ == "__main__":
    blocks = [
        """
- This is an ul
- This is a second one
- This is a third one
""",
        "###### This is a heading",
        """
```
This is a code block
That should span over multiple lines
""",
        """
1. Ordered list
2. Ordered list
Ordered list
""",
        ">this is a quote\nnot a quote",
    ]
    for i in blocks:
        print(block_to_block_type(i))

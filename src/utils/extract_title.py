from utils.markdown_to_blocks import markdown_to_blocks
from utils.block_to_block_type import block_to_block_type, BlockType


def extract_title(md):
    blocks = markdown_to_blocks(md)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type != BlockType.HEADING:
            continue
        hashtags, title = block.split(" ", 1)
        heading_level = len(hashtags)
        if heading_level == 1:
            return title
    raise Exception("no h1 header found.")

def markdown_to_blocks(text):
    split_by_line = text.split("\n\n")
    clean_blocks = []
    for line in split_by_line:
        if line:
            clean_blocks.append(line.strip())
    return clean_blocks

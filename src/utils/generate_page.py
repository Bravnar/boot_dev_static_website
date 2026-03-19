import os
from utils.markdown_to_html import markdown_to_html_node
from utils.extract_title import extract_title
from pprint import pprint


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_abs = os.path.abspath(from_path)
    template_abs = os.path.abspath(template_path)
    dest_abs = os.path.abspath(dest_path)

    with open(from_abs, "r") as f:
        from_content = str(f.read())

    with open(template_abs, "r") as t:
        template_content = str(t.read())

    # pprint(from_content)

    title = extract_title(from_content)
    node = markdown_to_html_node(from_content)
    html_string = node.to_html()
    to_write = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_string
    )
    with open(dest_abs, "w") as d:
        d.write(to_write)

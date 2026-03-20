import os

from utils.generate_page import generate_page


def recursive_generate(src, template, dest):
    list_to_generate = os.listdir(src)
    for item in list_to_generate:
        abs_path = os.path.join(src, item)
        if os.path.isfile(abs_path):
            dest_title = item.replace(".md", ".html")
            dest_path = os.path.join(dest, dest_title)
            generate_page(abs_path, template, dest_path)
        elif os.path.isdir(abs_path):
            new_dir_path = os.path.join(dest, item)
            os.mkdir(new_dir_path)
            recursive_generate(abs_path, template, new_dir_path)


def generate_pages_recursive(src_dir, template_path, dest_dir):
    print("Calling generate pages recurrsive")
    src_abs = os.path.abspath(src_dir)
    template_abs = os.path.abspath(template_path)
    dest_abs = os.path.abspath(dest_dir)
    if not (os.path.exists(src_abs) and os.path.isdir(src_abs)):
        raise Exception("source directory does not exist or is not a directory")
    recursive_generate(src_abs, template_abs, dest_abs)

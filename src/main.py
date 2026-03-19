import os
import shutil


def recursive_copy(to_copy, dest):
    list_to_copy = os.listdir(to_copy)
    for item in list_to_copy:
        abs_path = os.path.join(to_copy, item)
        if os.path.isfile(abs_path):
            shutil.copy(abs_path, os.path.join(dest, item))
        elif os.path.isdir(abs_path):
            new_dir_path = os.path.join(dest, item)
            os.mkdir(new_dir_path)
            recursive_copy(abs_path, new_dir_path)


def static_to_public(src="static/", dest="public/"):
    print("Calling static to public function")
    src_abs = os.path.abspath(src)
    dest_abs = os.path.abspath(dest)
    # print(src_abs, dest_abs, sep="\n")
    if not (os.path.exists(src_abs) and os.path.isdir(src_abs)):
        raise Exception("source directory does not exist or is not a directory")
    if os.path.exists(dest_abs) and os.path.isdir(dest_abs):
        shutil.rmtree(dest_abs)
    os.mkdir(dest_abs)
    recursive_copy(src_abs, dest_abs)


def main():
    print("Welcome to the Static Website Generator")
    static_to_public()


if __name__ == "__main__":
    main()

import sys
from utils.generate_pages_recursive import generate_pages_recursive
from utils.static_to_public import static_to_public


def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(base_path)
    print("Welcome to the Static Website Generator")
    static_to_public()
    generate_pages_recursive("content", "template.html", "docs", base_path)


if __name__ == "__main__":
    main()

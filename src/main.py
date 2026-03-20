from utils.generate_pages_recursive import generate_pages_recursive
from utils.static_to_public import static_to_public
from utils.generate_page import generate_page


def main():
    print("Welcome to the Static Website Generator")
    static_to_public()
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()

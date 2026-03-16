from nodes.textnode import TextNode, TextType
from utils.split_nodes_delimiter import split_nodes_delimiter
from pprint import pprint


def main():
    # new_text_node = TextNode(
    #     "This is some anchor text", TextType.LINK, "https://boot.dev"
    # )
    # print(new_text_node)
    print("############# Testing split_nodes_delimiter")

    nodes = [
        TextNode("This phrase has **one** word that is bold", TextType.TEXT),
        TextNode("This **one** here has **two** words that are bold", TextType.TEXT),
        TextNode(
            "This **one** here has **three** words that are **bold**", TextType.TEXT
        ),
        # TextNode("This **node should fail.", TextType.TEXT),
        TextNode("This *node* should not count.", TextType.TEXT),
    ]
    try:
        pprint(split_nodes_delimiter(nodes, "**", TextType.BOLD))
    except Exception as e:
        print(f"Whoops you hit an {e}")


if __name__ == "__main__":
    main()

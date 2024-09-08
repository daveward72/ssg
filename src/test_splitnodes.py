import unittest

from textnode import TextNode
from splitnodes import *

class TestSplitNodes(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("This is text with a ", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[0].text_type)
        self.assertEqual("code block", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_code, new_nodes[1].text_type)
        self.assertEqual(" word", new_nodes[2].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[2].text_type)

    def test_bold(self):
        node = TextNode("This is text with some **bold text** in the middle and at the **end**", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", TextNode.text_type_bold)
        self.assertEqual(4, len(new_nodes))
        self.assertEqual("This is text with some ", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[0].text_type)
        self.assertEqual("bold text", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_bold, new_nodes[1].text_type)
        self.assertEqual(" in the middle and at the ", new_nodes[2].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[2].text_type)
        self.assertEqual("end", new_nodes[3].text)
        self.assertEqual(TextNode.text_type_bold, new_nodes[3].text_type)

    def test_italic(self):
        node = TextNode("*Some italic* text to start, some in the *middle* and some at the *end*", TextNode.text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", TextNode.text_type_italic)
        self.assertEqual(5, len(new_nodes))
        self.assertEqual("Some italic", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_italic, new_nodes[0].text_type)
        self.assertEqual(" text to start, some in the ", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[1].text_type)
        self.assertEqual("middle", new_nodes[2].text)
        self.assertEqual(TextNode.text_type_italic, new_nodes[2].text_type)
        self.assertEqual(" and some at the ", new_nodes[3].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[3].text_type)
        self.assertEqual("end", new_nodes[4].text)
        self.assertEqual(TextNode.text_type_italic, new_nodes[4].text_type)
    
    def test_mixed_nodes(self):
        nodes = [
            TextNode("This is a link", TextNode.text_type_link, "http://wwww.google.com"),
            TextNode("This is text with some **bold text** in the middle and at the **end**", TextNode.text_type_text),
            TextNode("This is an image", TextNode.text_type_image, "http://wwww.davetest.com/imgages/cat.jpg"),
            TextNode("This is some text with nothing bolded", TextNode.text_type_text)          
        ]

        new_nodes = split_nodes_delimiter(nodes, "**", TextNode.text_type_bold)
        self.assertEqual(7, len(new_nodes))
        self.assertEqual("This is a link", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_link, new_nodes[0].text_type)
        self.assertEqual("This is text with some ", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[1].text_type)
        self.assertEqual("bold text", new_nodes[2].text)
        self.assertEqual(TextNode.text_type_bold, new_nodes[2].text_type)
        self.assertEqual(" in the middle and at the ", new_nodes[3].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[3].text_type)
        self.assertEqual("end", new_nodes[4].text)
        self.assertEqual(TextNode.text_type_bold, new_nodes[4].text_type)
        self.assertEqual("This is an image", new_nodes[5].text)
        self.assertEqual(TextNode.text_type_image, new_nodes[5].text_type)
        self.assertEqual("This is some text with nothing bolded", new_nodes[6].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[6].text_type)

    def test_images(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextNode.text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(4, len(new_nodes))
        self.assertEqual("This is text with a ", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[0].text_type)
        self.assertEqual("rick roll", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_image, new_nodes[1].text_type)
        self.assertEqual("https://i.imgur.com/aKaOqIh.gif", new_nodes[1].url)
        self.assertEqual(" and ", new_nodes[2].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[2].text_type)
        self.assertEqual("obi wan", new_nodes[3].text)
        self.assertEqual(TextNode.text_type_image, new_nodes[3].text_type)
        self.assertEqual("https://i.imgur.com/fJRm4Vk.jpeg", new_nodes[3].url)

    def test_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextNode.text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(4, len(new_nodes))
        self.assertEqual("This is text with a link ", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[0].text_type)
        self.assertEqual("to boot dev", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_link, new_nodes[1].text_type)
        self.assertEqual("https://www.boot.dev", new_nodes[1].url)
        self.assertEqual(" and ", new_nodes[2].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[2].text_type)
        self.assertEqual("to youtube", new_nodes[3].text)
        self.assertEqual(TextNode.text_type_link, new_nodes[3].text_type)
        self.assertEqual("https://www.youtube.com/@bootdotdev", new_nodes[3].url)

    def test_start_with_image(self):
        node = TextNode("![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) asdf", TextNode.text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(2, len(new_nodes))
        self.assertEqual("obi wan", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_image, new_nodes[0].text_type)
        self.assertEqual("https://i.imgur.com/fJRm4Vk.jpeg", new_nodes[0].url)
        self.assertEqual(" asdf", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[1].text_type)

    def test_only_image(self):
        node = TextNode("![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextNode.text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(1, len(new_nodes))
        self.assertEqual("obi wan", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_image, new_nodes[0].text_type)
        self.assertEqual("https://i.imgur.com/fJRm4Vk.jpeg", new_nodes[0].url)

    def test_only_text_split_image(self):
        node = TextNode("There is no image here", TextNode.text_type_text)
        new_nodes = split_nodes_image([node])
        self.assertEqual(1, len(new_nodes))
        self.assertEqual("There is no image here", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[0].text_type)

    def test_start_with_link(self):
        node = TextNode("[to boot dev](https://www.boot.dev) asdf", TextNode.text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(2, len(new_nodes))
        self.assertEqual("to boot dev", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_link, new_nodes[0].text_type)
        self.assertEqual("https://www.boot.dev", new_nodes[0].url)
        self.assertEqual(" asdf", new_nodes[1].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[1].text_type)

    def test_only_link(self):
        node = TextNode("[to boot dev](https://www.boot.dev)", TextNode.text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(1, len(new_nodes))
        self.assertEqual("to boot dev", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_link, new_nodes[0].text_type)
        self.assertEqual("https://www.boot.dev", new_nodes[0].url)

    def test_only_text_split_link(self):
        node = TextNode("There is no link here", TextNode.text_type_text)
        new_nodes = split_nodes_link([node])
        self.assertEqual(1, len(new_nodes))
        self.assertEqual("There is no link here", new_nodes[0].text)
        self.assertEqual(TextNode.text_type_text, new_nodes[0].text_type)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(10, len(nodes))
        self.assertEqual("This is ", nodes[0].text)
        self.assertEqual(TextNode.text_type_text, nodes[0].text_type)
        self.assertEqual("text", nodes[1].text)
        self.assertEqual(TextNode.text_type_bold, nodes[1].text_type)
        self.assertEqual(" with an ", nodes[2].text)
        self.assertEqual(TextNode.text_type_text, nodes[2].text_type)
        self.assertEqual("italic", nodes[3].text)
        self.assertEqual(TextNode.text_type_italic, nodes[3].text_type)
        self.assertEqual(" word and a ", nodes[4].text)
        self.assertEqual(TextNode.text_type_text, nodes[4].text_type)
        self.assertEqual("code block", nodes[5].text)
        self.assertEqual(TextNode.text_type_code, nodes[5].text_type)
        self.assertEqual(" and an ", nodes[6].text)
        self.assertEqual(TextNode.text_type_text, nodes[6].text_type)
        self.assertEqual("obi wan image", nodes[7].text)
        self.assertEqual(TextNode.text_type_image, nodes[7].text_type)
        self.assertEqual("https://i.imgur.com/fJRm4Vk.jpeg", nodes[7].url)
        self.assertEqual(" and a ", nodes[8].text)
        self.assertEqual(TextNode.text_type_text, nodes[8].text_type)
        self.assertEqual("link", nodes[9].text)
        self.assertEqual(TextNode.text_type_link, nodes[9].text_type)
        self.assertEqual("https://boot.dev", nodes[9].url)

if __name__ == "__main__":
    unittest.main()
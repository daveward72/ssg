import unittest

from textnode import TextNode
from converter import *

class TestConverter(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("Hello", TextNode.text_type_text)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(None, leaf_node.tag)
        self.assertEqual("Hello", leaf_node.value)

    def text_bold(self):
        bold_node = TextNode("This is some bold text", TextNode.text_type_bold)
        leaf_node = text_node_to_html_node(bold_node)
        self.assertEqual("b", leaf_node.tag)
        self.assertEqual("This is some bold text", leaf_node.value)

    def test_italic(self):
        italic_node = TextNode("This is some italic text", TextNode.text_type_italic)
        leaf_node = text_node_to_html_node(italic_node)
        self.assertEqual("i", leaf_node.tag)
        self.assertEqual("This is some italic text", leaf_node.value)

    def test_code(self):
        code_node = TextNode("This is some code", TextNode.text_type_code)
        leaf_node = text_node_to_html_node(code_node)
        self.assertEqual("code", leaf_node.tag)
        self.assertEqual("This is some code", leaf_node.value)

    def test_link(self):
        link_node = TextNode("This is a link", TextNode.text_type_link, "https://www.boot.dev")
        leaf_node = text_node_to_html_node(link_node)
        self.assertEqual("a", leaf_node.tag)
        self.assertEqual("This is a link", leaf_node.value)
        self.assertEqual("https://www.boot.dev", leaf_node.props["href"])

    def test_image(self):
        image_node = TextNode("Alt text", TextNode.text_type_image, "https://davetest/images/img1.gif")
        leaf_node = text_node_to_html_node(image_node)
        self.assertEqual("img", leaf_node.tag)
        self.assertEqual("", leaf_node.value)
        self.assertEqual("https://davetest/images/img1.gif", leaf_node.props["src"])
        self.assertEqual("Alt text", leaf_node.props["alt"])

    def test_paragraph(self):
        markdown = "This is just some text with **bold** content thrown in for fun"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual('div', html_node.tag)
        p_node = html_node.children[0]
        self.assertEqual('p', p_node.tag)
        self.assertEqual(3, len(p_node.children))
        self.assertEqual(None, p_node.children[0].tag)
        self.assertEqual("This is just some text with ", p_node.children[0].value)
        self.assertEqual("b", p_node.children[1].tag)
        self.assertEqual("bold", p_node.children[1].value)
        self.assertEqual(None, p_node.children[2].tag)
        self.assertEqual(" content thrown in for fun", p_node.children[2].value)

    def test_heading(self):
        markdown = "### This is a heading\n\n"
        markdown += "This is some paragraph content"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual('div', html_node.tag)
        self.assertEqual(2, len(html_node.children))
        h3_node = html_node.children[0]
        p_node = html_node.children[1]
        self.assertEqual('h3', h3_node.tag)
        self.assertEqual(1, len(h3_node.children))
        self.assertEqual(None, h3_node.children[0].tag)
        self.assertEqual("This is a heading", h3_node.children[0].value)
        self.assertEqual('p', p_node.tag)
        self.assertEqual(1, len(p_node.children))
        self.assertEqual(None, p_node.children[0].tag)
        self.assertEqual("This is some paragraph content", p_node.children[0].value)

    def test_code(self):
        markdown = "```\n"
        markdown += "Code block\n"
        markdown += "```"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual('div', html_node.tag)
        code_node = html_node.children[0]
        self.assertEqual('code', code_node.tag)
        self.assertEqual(1, len(code_node.children))
        self.assertEqual(None, code_node.children[0].tag)
        self.assertEqual("Code block", code_node.children[0].value)


    def test_quote(self):
        markdown = "> line 1 of quoted text\n"
        markdown += "> line 2 of quoted text"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual('div', html_node.tag)
        quote_node = html_node.children[0]
        self.assertEqual('blockquote', quote_node.tag)
        self.assertEqual(1, len(quote_node.children))
        self.assertEqual(None, quote_node.children[0].tag)
        self.assertEqual("line 1 of quoted text\nline 2 of quoted text", quote_node.children[0].value)

    def test_unordered_list(self):
        markdown = "* list item 1\n"
        markdown += "* list item 2"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual('div', html_node.tag)
        ul_node = html_node.children[0]
        self.assertEqual('ul', ul_node.tag)
        self.assertEqual(2, len(ul_node.children))
        li_1 = ul_node.children[0]
        li_2 = ul_node.children[1]
        self.assertEqual('li', li_1.tag)
        self.assertEqual('li', li_2.tag)
        self.assertEqual(1, len(li_1.children))
        self.assertEqual(1, len(li_2.children))
        self.assertEqual(None, li_1.children[0].tag)
        self.assertEqual(None, li_2.children[0].tag)
        self.assertEqual("list item 1", li_1.children[0].value)
        self.assertEqual("list item 2", li_2.children[0].value)

    def test_ordered_list(self):
        markdown = "1. This is the first thing to do\n"
        markdown += "2. Some other thing to do"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual('div', html_node.tag)
        ol_node = html_node.children[0]
        self.assertEqual('ol', ol_node.tag)
        self.assertEqual(2, len(ol_node.children))
        li_1 = ol_node.children[0]
        li_2 = ol_node.children[1]
        self.assertEqual('li', li_1.tag)
        self.assertEqual('li', li_2.tag)
        self.assertEqual(1, len(li_1.children))
        self.assertEqual(1, len(li_2.children))
        self.assertEqual(None, li_1.children[0].tag)
        self.assertEqual(None, li_2.children[0].tag)
        self.assertEqual("This is the first thing to do", li_1.children[0].value)
        self.assertEqual("Some other thing to do", li_2.children[0].value)

if __name__ == "__main__":
    unittest.main()
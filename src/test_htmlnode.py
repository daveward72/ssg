import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_p(self):
        p_node = HTMLNode("p", "This is a test paragraph")
        self.assertEqual("p", p_node.tag)
        self.assertEqual("This is a test paragraph", p_node.value)

    def test_a(self):
        props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        a_node = HTMLNode("a", "boot.dev", props=props)
        self.assertEqual("a", a_node.tag)
        self.assertEqual("boot.dev", a_node.value)
        self.assertEqual("href=\"https://www.google.com\" target=\"_blank\"", a_node.props_to_html())

    def test_h1(self):
        h1_node = HTMLNode("h1", "This is a heading")
        self.assertEqual("h1", h1_node.tag)
        self.assertEqual("This is a heading", h1_node.value)
    
if __name__ == "__main__":
    unittest.main()
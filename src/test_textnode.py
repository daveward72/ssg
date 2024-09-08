import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", "bold", "http://www.google.com")
        node2 = TextNode("This is a text node", "bold", "http://www.google.com")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", "bold", "http://www.google.com")
        self.assertEqual("This is a text node", node.text)

    def test_text_type(self):
        node = TextNode("This is a text node", "italic", None)
        self.assertEqual("italic", node.text_type)

    def test_url(self):
        node = TextNode("This is a text node", "bold", "http://www.boot.dev")
        self.assertEqual("http://www.boot.dev", node.url)

    def test_not_equal(self):
        node = TextNode("This is a text node", "bold", "http://www.google.com")
        node2 = TextNode("This is a text node with different text", "bold", "http://www.google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
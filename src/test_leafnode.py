import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_p(self):
        p_leaf = LeafNode("p",  "This is a paragraph of text.")
        self.assertEqual("p", p_leaf.tag)
        self.assertEqual("This is a paragraph of text.", p_leaf.value)
        self.assertEqual("<p>This is a paragraph of text.</p>", p_leaf.to_html())

    def test_a(self):
        a_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual("a", a_leaf.tag)
        self.assertEqual("Click me!", a_leaf.value)
        self.assertEqual("href=\"https://www.google.com\"", a_leaf.props_to_html())
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>", a_leaf.to_html())

if __name__ == "__main__":
    unittest.main()
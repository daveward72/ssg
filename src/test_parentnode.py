import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_example_p(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_mult_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode("b", [LeafNode("i", "Bold italics text")]),
                LeafNode(None, "Normal text")
            ]
        )

        self.assertEqual("<p><b><i>Bold italics text</i></b>Normal text</p>", node.to_html())

    def test_parent_no_children(self):
        node = ParentNode("p", None)

        with self.assertRaises(ValueError):
            node.to_html()

    def test_missing_tag(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_children(self):
        node = ParentNode("p", [])

        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
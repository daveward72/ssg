import unittest

from blocks import *

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n"
        markdown += "\n"
        markdown += "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
        markdown += '\n'
        markdown += "* This is the first list item in a list block\n"
        markdown += "* This is a list item\n"
        markdown += "* This is another list item\n"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(3, len(blocks))
        self.assertEqual("# This is a heading", blocks[0])
        self.assertEqual("This is a paragraph of text. It has some **bold** and *italic* words inside of it.", blocks[1])
        self.assertEqual("* This is the first list item in a list block\n* This is a list item\n* This is another list item", blocks[2])

    def test_heading_block(self):
        block_type = block_to_block_type("## This is a heading")
        self.assertEqual("heading", block_type)

    def test_code_block(self):
        markdown = "```\n"
        markdown += "This is a code block\n"
        markdown += "```n"
        block_type = block_to_block_type(markdown)
        self.assertEqual("code", block_type)

    def test_quote_block(self):
        markdown = "> line 1 of quoted text\n"
        markdown += "> line 2 of quoted text"
        block_type = block_to_block_type(markdown)
        self.assertEqual('quote', block_type)

    def test_unordered_list_block(self):
        markdown = "* list item 1\n"
        markdown += "* list item 2"
        block_type = block_to_block_type(markdown)
        self.assertEqual('unordered_list', block_type)
    
    def test_ordered_list_block(self):
        markdown = "1. This is the first thing to do\n"
        markdown += "2. Some other thing to do"
        block_type = block_to_block_type(markdown)
        self.assertEqual('ordered_list', block_type)

    def test_ordered_list_start_at_2_block(self):
        markdown = "2. Starting not at the beginning for some reason"
        markdown += "1. Why not backtrack"
        block_type = block_to_block_type(markdown)
        self.assertEqual('paragraph', block_type)

    def test_paragraph_block(self):
        block_type = block_to_block_type("This is just some text")
        self.assertEqual('paragraph', block_type)

if __name__ == "__main__":

    unittest.main()
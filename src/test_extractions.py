import unittest

from extractions import *

class TestExtractions(unittest.TestCase):
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(2, len(extracted_images))
        self.assertEqual("rick roll", extracted_images[0][0])
        self.assertEqual("https://i.imgur.com/aKaOqIh.gif", extracted_images[0][1])
        self.assertEqual("obi wan", extracted_images[1][0])
        self.assertEqual("https://i.imgur.com/fJRm4Vk.jpeg", extracted_images[1][1])

    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(2, len(extracted_links))
        self.assertEqual("to boot dev", extracted_links[0][0])
        self.assertEqual("https://www.boot.dev", extracted_links[0][1])
        self.assertEqual("to youtube", extracted_links[1][0])
        self.assertEqual("https://www.youtube.com/@bootdotdev", extracted_links[1][1])

    def test_title(self):
        markdown = "# This Is The Title\n\n"
        markdown += "Then we have some nice paragraph text"
        title = extract_title(markdown)
        self.assertEqual("This Is The Title", title)

if __name__ == "__main__":
    unittest.main()
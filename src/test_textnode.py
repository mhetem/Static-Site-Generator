import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("this is a text", TextType.ITALIC)
        node2 = TextNode("this is a different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_texttype(self):
        node = TextNode("this is a text", TextType.ITALIC)
        node2 = TextNode("this is a different text", TextType.ITALIC)
        self.assertEqual(node.text_type, node2.text_type)


if __name__ == "__main__":
    unittest.main()
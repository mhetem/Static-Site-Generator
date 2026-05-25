import unittest
from htmlnode import *
from textnode import *
from functions import *

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_no_delimiter(self):
        nodes = [
            TextNode("this a plain text",TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**",TextType.TEXT)
        expected = [TextNode("this a plain text",TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_single_code_block(self):
        nodes = [
            TextNode("this a plain `code block` text",TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "`",TextType.CODE)
        expected = [
            TextNode("this a plain ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test__multiple_bold_sections(self):
        nodes = [
            TextNode("this a plain text with multiple **bold** words **inside** it.", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**",TextType.BOLD)
        expected = [
            TextNode("this a plain text with multiple ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" words ", TextType.TEXT),
            TextNode("inside", TextType.BOLD),
            TextNode(" it.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        nodes = [
            "this an _unmatched test"
        ]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "_",TextType.ITALIC)    

        
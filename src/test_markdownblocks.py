import unittest
from htmlnode import *
from textnode import *
from functions import *
from markdown_blocks import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_heading(self):
        block = "## Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_wrong_heading(self):
        block = "####### Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code(self):
        block = "```\nHello world\n```"  
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_quote_nospace(self):
        block = ">Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        

    def test_unordered_list(self):
        block = "- Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_several(self):
        block = "- Hello world\n- another\n- yet another"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_several(self):
        block = "1. Hello world\n2. another\n3. yet another"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
from htmlnode import *
from textnode import *
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href":text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url,"alt": text_node.text})

    else:
        raise Exception("text type not acceptable")
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        if len(node.text.split(delimiter)) % 2 == 0:
            raise Exception("second delimiter not found")
        splitted = node.text.split(delimiter)
        
        for i, strings in enumerate(splitted):
            if i % 2 == 0:
            
                new_string = TextNode(strings, TextType.TEXT)
                new_list.append(new_string)
            
            else:
                new_string = TextNode(strings, text_type)
                new_list.append(new_string)
         
    
    return new_list
            

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        images = extract_markdown_images(node.text)
        original_text = node.text
        if len(images) == 0:
            new_list.append(node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections[0]) != 0:
                new_list.append(TextNode(sections[0],TextType.TEXT))
            new_list.append(TextNode(image[0],TextType.IMAGE,image[1]))
            original_text = sections[1]
        if len(original_text) != 0:
            new_list.append(TextNode(original_text, TextType.TEXT))        

    
    return new_list


def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        images = extract_markdown_links(node.text)
        original_text = node.text
        if len(images) == 0:
            new_list.append(node)
            continue
        for image in images:
            sections = original_text.split(f"[{image[0]}]({image[1]})", 1)
            if len(sections[0]) != 0:
                new_list.append(TextNode(sections[0],TextType.TEXT))
            new_list.append(TextNode(image[0],TextType.LINK,image[1]))
            original_text = sections[1]
        if len(original_text) != 0:
            new_list.append(TextNode(original_text, TextType.TEXT))        

    
    return new_list
    
def text_to_textnodes(text):
    new_list = [TextNode(text, TextType.TEXT)]
    new_list = split_nodes_delimiter(new_list, "**", TextType.BOLD)
    new_list = split_nodes_delimiter(new_list, "_", TextType.ITALIC)
    new_list = split_nodes_delimiter(new_list, "`", TextType.CODE)
    new_list = split_nodes_image(new_list)
    new_list = split_nodes_link(new_list)
    return new_list


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_list = []
    for block in blocks:
        stripped = block.strip()
        if stripped == "":
            continue
        new_list.append(stripped)
    return new_list
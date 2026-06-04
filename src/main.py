from textnode import TextNode
from textnode import TextType
from copystatic import copy_files_recursive
import os
import shutil
from generate_page import *

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_files_recursive("./static", "./public")
    generate_page_recursive("./content", "./template.html", "./public")


    

main()
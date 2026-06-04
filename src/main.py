from textnode import TextNode
from textnode import TextType
from copystatic import copy_files_recursive
import os
import shutil
from generate_page import *
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    copy_files_recursive("./static", "./docs")
    generate_page_recursive("./content", "./template.html", "./docs", basepath)


    

main()
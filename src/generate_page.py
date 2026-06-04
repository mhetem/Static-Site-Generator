from functions import *
from markdown_blocks import *
from extract_title_mkdw import *
import os
from pathlib import Path


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as t:
        template = t.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    result = template.replace("{{ Title }}", title)
    result = result.replace("{{ Content }}", html)
    result = result.replace('href="/', f'href="{basepath}')
    result = result.replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as d:
        d.write(result)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dirs = os.listdir(dir_path_content)
    for dir in dirs:
        fullpath = os.path.join(dir_path_content, dir)
        if os.path.isfile(fullpath):
            dest_file_path = os.path.join(dest_dir_path, dir)
            html_dest_path = Path(dest_file_path).with_suffix(".html")
            generate_page(fullpath, template_path, html_dest_path, basepath)
        else:
            generate_page_recursive(fullpath, template_path, os.path.join(dest_dir_path, dir), basepath)




        


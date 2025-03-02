import shutil
import os
import os.path
import pathlib
import sys

from converter import *

from textnode import TextNode

def copy_contents(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    for entry in os.listdir(source):
        source_path = os.path.join(source, entry)
        dest_path = os.path.join(destination, entry)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"copied {source_path} to {dest_path}")
        elif os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_contents(source_path, dest_path)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        from_content = file.read()

    with open(template_path, 'r') as file:
        template_content = file.read()

    htmlContent = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    html_page_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", htmlContent)
    html_page_content = html_page_content.replace('href="/', f'href="{basepath}')
    html_page_content = html_page_content.replace('src="/', f'src="{basepath}')
    os.makedirs(os.path.split(dest_path)[0], exist_ok=True)
    open(dest_path, 'w').write(html_page_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print('generate_pages_recursive')
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(entry_path) and pathlib.Path(entry).suffix == ".md":
            new_filename = f"{os.path.splitext(entry)[0]}.html"
            dest_path = os.path.join(dest_dir_path, new_filename)
            print('call generate_page')
            generate_page(entry_path, './template.html', dest_path, basepath)
        elif os.path.isdir(entry_path):
            dest_path = os.path.join(dest_dir_path, entry)
            os.mkdir(dest_path)
            generate_pages_recursive(entry_path, template_path, dest_path, basepath)

def main():
    basepath = '/'
    if len(sys.argv) >=2:
        basepath = sys.argv[1]

    copy_contents('./static', './docs')
    #generate_page('./content/index.md', './template.html', './public/index.html')
    generate_pages_recursive('./content', './template.html', './docs', basepath)

main()
import re

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
   return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def extract_title(markdown):
    lines = markdown.split('\n')
    line_match = list(filter(lambda ln:len(ln) > 1 and ln[:2] == "# ", lines))
    if len(line_match) == 0:
        raise Exception("no title")
    return line_match[0].split("# ", 1)[1]
from textnode import TextNode

from extractions import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextNode.text_type_text:
            split_parts = node.text.split(delimiter)

            if len(split_parts) % 2 == 0:
                raise Exception(f"invalid markdown syntax. unclosed delimiter: {delimiter}")
            
            for i in range(len(split_parts)):
                part = split_parts[i]

                if len(part) > 0:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(part, TextNode.text_type_text))
                    else:
                        new_nodes.append(TextNode(part, text_type))
        else:
            new_nodes.append(node)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextNode.text_type_text:
            images = extract_markdown_images(node.text)
            remaining_text = node.text
            for image in images:
                image_alt = image[0]
                image_link = image[1]
                sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
                new_nodes.append(TextNode(image_alt, TextNode.text_type_image, image_link))
                remaining_text = sections[1]
            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextNode.text_type_text))
        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextNode.text_type_text:
            links = extract_markdown_links(node.text)
            remaining_text = node.text
            for link in links:
                link_text = link[0]
                link_url = link[1]
                sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextNode.text_type_text))
                new_nodes.append(TextNode(link_text, TextNode.text_type_link, link_url))
                remaining_text = sections[1]
            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextNode.text_type_text))
        else:
            new_nodes.append(node)

    return new_nodes

def text_to_textnodes(text):
    single_node = TextNode(text, TextNode.text_type_text)
    nodes = [single_node]
    nodes = split_nodes_delimiter(nodes, "**", TextNode.text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", TextNode.text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", TextNode.text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
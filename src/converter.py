from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from splitnodes import *

from blocks import *

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case TextNode.text_type_text:
            return LeafNode(value=text_node.text)
        case TextNode.text_type_bold:
            return LeafNode("b", text_node.text)
        case TextNode.text_type_italic:
            return LeafNode("i", text_node.text)
        case TextNode.text_type_code:
            return LeafNode("code", text_node.text)
        case TextNode.text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextNode.text_type_image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("invalid text_type")
        
def text_nodes_to_html_nodes(text_nodes):
    return list(
        map(lambda node:text_node_to_html_node(node), text_nodes)
    )
        
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlNodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "paragraph":
                text_nodes = text_to_textnodes(block)
                htmlNode = ParentNode('p', text_nodes_to_html_nodes(text_nodes))
            case "heading":
                text = heading_block_text(block)
                heading_tag = get_heading_tag(block)
                text_nodes = text_to_textnodes(text)
                htmlNode = ParentNode(heading_tag, text_nodes_to_html_nodes(text_nodes))
            case "code":
                text = code_block_text(block)
                text_nodes = text_to_textnodes(text)
                htmlNode = ParentNode('code', text_nodes_to_html_nodes(text_nodes))
            case "quote":
                text = quote_block_text(block)
                text_nodes = text_to_textnodes(text)
                htmlNode = ParentNode('blockquote', text_nodes_to_html_nodes(text_nodes))
            case "unordered_list":
                text_items = get_list_text_items(block)
                htmlNode = ParentNode('ul', [])
                for text_item in text_items:

                    text_nodes = text_to_textnodes(text_item)
                    listItemNode = ParentNode("li",  text_nodes_to_html_nodes(text_nodes))
                    htmlNode.children.append(listItemNode)
            case "ordered_list":
                text_items = get_list_text_items(block)
                htmlNode = ParentNode('ol', [])
                for text_item in text_items:
                    text_nodes = text_to_textnodes(text_item)
                    listItemNode = ParentNode("li", text_nodes_to_html_nodes(text_nodes))
                    htmlNode.children.append(listItemNode)
            case _:
                raise ValueError("invalid block type")
        
        htmlNodes.append(htmlNode)

    return ParentNode('div', htmlNodes)

def heading_block_text(block):
    return block.split(' ', 1)[1]

def code_block_text(block):
    return block[3:-3].strip()

def quote_block_text(block):
    lines = block.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i][1:].strip()
    return '\n'.join(lines)

def get_list_text_items(block):
    lines = block.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ', 1)[1].strip()
    return lines

def get_heading_tag(block):
    h_num = 0
    indx = 0
    while block[indx] == '#':
        h_num += 1
        indx += 1
    return 'h' + str(h_num)
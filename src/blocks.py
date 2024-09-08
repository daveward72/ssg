import re

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    return list(map(lambda block:block.strip(), 
               filter(lambda block:len(block) > 0, blocks)
            ))

def block_to_block_type(block):
    lines = block.split('\n')
    numlines = len(lines)
   
    if re.match(r"#{1,6} .*", block):
        return "heading"
    elif re.match("```\s*(.*?)\s*```", block):
        return "code"
    elif len(list(filter(
        lambda line:len(line) > 0 and line[0] == '>', lines
        ))) == numlines:
        return "quote"
    elif len(list(filter(
        lambda line:len(line) > 0 and (line[:2] == '* ' or line[:2] == '- '), lines
        ))) == numlines:
        return "unordered_list"
    elif isordered_list(lines):
        return "ordered_list"
    else:
        return "paragraph"
    
def isordered_list(lines):
    for i in range(len(lines)):
        line = lines[i]
        if not '. ' in line:
            return False
        line_split = line.split('. ')
        num_part = line_split[0]
        if not num_part.isdigit() or int(num_part) != i+1:
            return False
        
    return True
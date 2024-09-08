from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag is required")
        
        if self.children == None or len(self.children) == 0:
            raise ValueError("children are required")
        
        html = "<" + self.tag
        if self.props:
            html += " " + self.props_to_html()
        html += ">"
        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html
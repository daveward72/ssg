from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag != "img" and not self.value:
            raise ValueError("value is required")
        
        if self.tag == None:
            return self.value
        
        html = "<" + self.tag
        if self.props:
            html += " " + self.props_to_html()
        html += f">{self.value}</{self.tag}>"
        
        return html
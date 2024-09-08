class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        retVal = ""
        for prop in self.props:
            if len(retVal) > 0:
                retVal += " "
            retVal += f"{prop}=\"{self.props[prop]}\""
        
        return retVal
    
    def __repr__(self):
        return f"HtmlNode(tag={self.tag}), value={self.value}, children={self.children}, props={self.props})"
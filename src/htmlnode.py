class HTMLNode:
    def __init__(self, tag: str= None, value: str= None, children: list= None, props: dict= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        end_string = ""
        if self.props is not None:
            for key in self.props:
                value = self.props[key]
                end_string += f' {key}="{value}"'
            return end_string
        return end_string
    
    def __repr__(self):
        return f"tag={self.tag}\nvalue={self.value}\nchildren={self.children}\nprops={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"tag={self.tag}\nvalue={self.value}\nprops={self.props}"
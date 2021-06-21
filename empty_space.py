class Empty_Space: 
    def __init__(self, position=None): 
        self.name = "Empty Space"
        self.alias = " "
        self.color = None
        self.position = position
        
    def __repr__(self): 
        return self.name

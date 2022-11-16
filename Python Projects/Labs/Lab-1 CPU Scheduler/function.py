class Function:
    def __init__(self, name, exception_handler="no"):
        self.name=name
        self.flag= exception_handler
        

    def __str__(self):
        return self.name

    
    

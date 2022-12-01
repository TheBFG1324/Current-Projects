#executive.py
class Executive:
    def __init__(self, inp):
        inp=open(inp, "r")
        self.matrix=[]

        for line in inp:
            self.matrix.append(line.split())
            


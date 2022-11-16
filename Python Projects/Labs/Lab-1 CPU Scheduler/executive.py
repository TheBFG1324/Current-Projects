
class Executive:
    def __init__(self):
        input_file=input("Enter file name: ")
        self._input=open(input_file)
        self.matrix=[]
        for line in self._input:
            info=line.split(" ")
            counter=0
            for element in info:
                if element.count("\n")>=1:
                    info[counter]=element.replace("\n", "")
                counter+=1
            self.matrix.append(info)
        
    
            


        

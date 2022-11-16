'''
Cameron Denton
2981510
date: 10/3/22
last mod: 10/4/22
Purpose: to create the blob class that holds member variables that can be edited using recursion. Does the required actions as required by the lab
'''
from executive import Executive
class Blob:
    def __init__(self):
        input_file=input("Enter file: ")
        blob=Executive(input_file)
        self.start=(blob.matrix[1][0], blob.matrix[1][1])
        self.city=blob.get_city()
        self.matrix=blob.get_matrix()
        self.move=1
        self.sewers=[]
        self.total_people=0
        self.sewer_access=False

        for x in range(len(self.city)):
            for y in range(len(self.city[0])):
                if self.city[x][y]=="@":
                    tup=(x,y)
                    self.sewers.append(tup)
        
        
    def is_valid_move(self,row, colm):
        if 0<=colm<=len(self.city[0])-1:
            if 0<=row<=len(self.city)-1:
                if self.city[row][colm]=="S" or self.city[row][colm]=="P" or self.city[row][colm]=="@":
                    return True
                else:
                    return False

            else: return False

        else:
            return False

    

    def consume(self,row,colm):
        if self.city[row][colm]=='P':
            self.total_people+=1
            self.city[row][colm]="B"

        elif self.city[row][colm]=='@':
            self.sewer_access=True

        else:
            self.city[row][colm]="B"
            
            
            
        
        

    def my_move(self, row, colm):
            
        

        if self.is_valid_move(row,colm):
            self.consume(row,colm)
        

            if self.my_move(row-1,colm):
                return #True

            if self.my_move(row, colm+1):
                return #True

            if self.my_move(row+1,colm):
                return #True

            if self.my_move(row,colm-1):
                return #True
            

        else:
            return False
    def run1(self):
        self.my_move(int(self.start[0]),int(self.start[1]))
        for i in range(len(self.sewers)):
            if self.sewer_access==True:
                self.my_move(int(self.sewers[i][0]),int(self.sewers[i][1]))
        print(self.matrix[0][0]+ " "+self.matrix[0][1]+"\n"+self.matrix[1][0]+ " "+self.matrix[1][1])
        x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.city])
        print(x)
        print("Total Eaten: "+ str(self.total_people))
                
            
        
    
        











        



'''
Cameron Denton
2981510
date: 10/3/22
last mod: 10/4/22
Purpose: does all the file handling and processing to become readable for the blob class
'''
#executive.py
class Executive:
    def __init__(self, input_file):
        self.input=open(input_file, "r")
        self.matrix=[]
        for line in self.input:
            line=line.strip()
            self.matrix.append(line.split())

        num_rows=0
        num_colm=0

        if int(self.matrix[0][0])>=0:
            num_rows=int(self.matrix[0][0])
        else:
            raise IndexError("Index is out of range")

        if int(self.matrix[0][1])>=0:
            num_colm=int(self.matrix[0][1])
        else:
            raise IndexError("Index is out of range")
        
        temp=[]
        for x in range(2, len(self.matrix)):
            new_word=self.matrix[x][0]
            temp.append(new_word)


        self.city=[]
        for elem in temp:
            word=elem
            new_word=[]
            for letter in word:
                new_word.append(letter)
            self.city.append(new_word)

        self.visted=[]
        for x in range(num_rows):
            row=[]
            for y in range(num_colm):
                row.append("")
            self.visted.append(row)
        self.visted[int(self.matrix[1][0])][int(self.matrix[1][1])]="0"

    def get_visted(self):
        return self.visted

    def get_city(self):
        return self.city

    def get_matrix(self):
        return self.matrix

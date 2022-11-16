'''
Cameron Denton
2981510
9/19/22
last Mod: 9/20/22
Purpose: takes input file and process it, then runs all the given commands from the file
'''
from browser import Browser
class Executive:
    def __init__(self):
        file=input("Enter file: ")
        file=open(file, "r")
        self.matrix=[]
        browser=Browser()
        for line in file:
            self.matrix.append(line.split())
        

        for element in self.matrix:
            if element[0]=="NAVIGATE":
                browser.navigate(element[1])

            elif element[0]=="HISTORY":
                browser.history()

            elif element[0]=="BACK":
                browser.backwards()

            elif element[0]=="FORWARD":
                browser.forward()

            else:
                print("Invalid Entry")


                
                



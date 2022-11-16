'''
Cameron Denton
2981510
9/19/22
last Mod: 9/20/22
Purpose: does all the processing for the different methods
'''
from linkedlist import LinkedList
class Browser:
    def __init__(self):
        self.list=LinkedList()
        self.current=None

    def navigate(self, url):
        if self.current==None:
            self.list.insert(0, url)
            self.current=0

        else:
            self.current+=1
            self.list.insert(self.current, url)
            for i in range(self.current+1, self.list.length()):
                self.list.remove(self.current+1)


            
                    

    def forward(self):
        if self.current+1<self.list.length():
            self.current+=1
        

    def backwards(self):
        if self.current>0:
            self.current-=1

        

    def history(self):

        print("OLDEST\n =======================\n")
        for i in range(self.list.length()):
            if i==self.current:
                print(str(self.list.get_entry(self.current))+"<===========")

            else:
                print(str(self.list.get_entry(i)))
        print("\nNewest\n =======================")



            
    

'''
Cameeron Denton
2981510
mast mod: 10/18/22
Purpose: popping an item from a stack
'''
import time
from linkedlist import LinkedList

i = LinkedList()
for x in range(100000):
    i.insert(x,1)


for x in range(1000, 101000,1000):
    start_time = time.process_time_ns()
    i.get_entry(x)
    end_time = time.process_time_ns()
    print(end_time - start_time)
        
        
    

print("Finished")

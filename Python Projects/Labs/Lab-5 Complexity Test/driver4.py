'''
Cameeron Denton
2981510
mast mod: 10/18/22
Purpose: popping an item from a stack
'''
import time
from linkedlist import LinkedList

i = LinkedList()
key = True
counter = 1000
while key:
    
    if counter <= 100000:
        for x in range(counter):
            
            i.insert(x, x)
        start_time = time.process_time_ns()
        i.get_entry(0)
        end_time = time.process_time_ns()
        print(end_time - start_time)
        for x in range(counter):
            i.remove(x)
        counter += 1000
    else:
        key = False

print("Finished")

'''
Cameeron Denton
2981510
mast mod: 10/18/22
Purpose: popping an item from a stack
'''
import time
from linkedqueue import LinkedQueue


key = True
counter = 1000

i = LinkedQueue()

while key is True:
    if counter <= 100000:
        start_time = time.process_time_ns()
        for x in range(counter):
            i.enqueue(x)
        end_time = time.process_time_ns()
        print(str(end_time - start_time))

        for x in range(counter):
            i.dequeue()
        counter += 1000
        key = True
    else:
        key = False
print("Finished")

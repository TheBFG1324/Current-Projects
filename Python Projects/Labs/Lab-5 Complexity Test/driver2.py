'''
Cameeron Denton
2981510
mast mod: 10/18/22
Purpose: popping an item from a stack
'''
import time
from linkedstack import LinkedStack

i = LinkedStack()
for x in range(100000):
    i.push(x)

counter = 35000
key = True
while key == True:

    if counter > 100000:
        key = False

    else:

        start_time = time.process_time_ns()

        for x in range(counter):
            i.pop()

        end_time = time.process_time_ns()
        print(end_time - start_time)

        for x in range(counter):
            i.push(x)
        counter += 1000

print("Finished")

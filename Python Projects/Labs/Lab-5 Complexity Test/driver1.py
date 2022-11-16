'''
Cameeron Denton
2981510
mast mod: 10/18/22
Purpose: popping an item from a stack
'''
import time
from linkedstack import LinkedStack

i = LinkedStack()
for x in range(70000):
    i.push(x)


def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns / BILLION


print("Beginning the timing code...")
start_time = time.process_time_ns()
i.pop()

end_time = time.process_time_ns()

print("Total time in ns: ", end_time - start_time)
print("Total time in sec: ", nanosec_to_sec(end_time - start_time))

#CPU-Schedule
from linkedqueue import LinkedQueue
from process import Process
from executive import Executive
from function import Function
class CPUSchedule:
    def __init__(self):
        self.queue=LinkedQueue()
        self.file=Executive()

    def process_enqueue(self, _process):
        self.queue.enqueue(_process)

    def process_dequeue(self):
        self.queue.dequeue()

    def schedule_setup(self):
        for element in self.file.matrix:
            if element[0]=="START":
                process=Process()
                process.name=element[1]
                self.queue.enqueue(process)
                print(process.name+" was added to the queue")
            
                

            if element[0]=="CALL":
                function=Function(element[1])
                function.name=element[1]
                if len(element)==3:
                    if element[2]=="yes":
                        function.flag="yes"
                self.queue.peek().process_push(function)
                print(self.queue.peek().name +" calls "+function.name)
                if self.queue._front==self.queue._back:
                    continue
                else:
                    self.process_enqueue(self.process_dequeue())
                

            if element[0]=="RETURN":
                if self.queue.peek().stack.peek()=="main":
                    print(self.queue.peek().name + " returns " + self.queue.peek().stack.peek())
                    print(self.queue.peek().name+ " process has ended")
                    self.queue.dequeue()
                else:
                    print(self.queue.peek().name + " returns " + self.queue.peek().stack.peek())
                    self.queue.peek().stack.pop()
                    self.process_enqueue(self.process_dequeue())
                    
                

            if element[0]=="RAISE":
                print(self.queue.peek().name+ " encountered a raised exception by: "+self.queue.peek().stack.peek().name)
                handle_exception=False
                process=self.queue.peek()
                func=process.stack.peek()
                can_handle=func.flag
                while self.queue.peek().stack.top is not None: 
                    
                    
                   
                    
                    if can_handle=="yes" or self.queue.peek().stack.peek() == 'main':
                        print("exception handled by: "+self.queue.peek().stack.peek())
                        self.queue.peek().stack.pop()

                    else:
                        print(self.queue.peek().name +" ends "+self.queue.peek().stack.peek().name+" due to unhandled exception ")
                        self.queue.peek().stack.pop()

                



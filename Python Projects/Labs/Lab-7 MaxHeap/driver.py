from executive import Executive
from maxheap import MaxHeap
from patient import Patient

def main():
    inp=input("Enter File Name: ")
    exec=Executive(inp)
    x=MaxHeap()
    for command in exec.matrix:
        try:
            if command[0]=="ARRIVE":
                new_patient=Patient(command)
                x.add(new_patient)
            elif command[0]=="NEXT":
                print(x.peek())
            elif command[0]=="TREAT":
                x.downheap()
            elif command[0]=="COUNT":
                print("There are "+str(x.count())+" patients left.")
        
            else:
                print("Invlaid Command was thrown")
        except:
            print("Invalid Command")
        print("------------------")
main()
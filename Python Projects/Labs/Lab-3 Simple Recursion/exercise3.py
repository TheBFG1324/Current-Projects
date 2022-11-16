'''
Cameron Denton
lab3 exercise 3
Date: 9/26/22
last Mod: 9/26/22
Purpose: to get a mode and number from user and either check if the number is in the fib sequence or get the ith number from fib sequence
'''
#exercise3
def fib(a):
    if a<0:
        return "invalid input"
    elif a==0:
        return 0

    elif a==1:
        return 1

    return fib(a-1)+fib(a-2)

def main():
    while True:
        inp=input("Enter mode and value: ")
        inp=inp.strip()
        inp=inp.split()

        if inp[0]=="-i":
            print(fib(int(inp[1])))

        elif inp[0]=="-v":
            index=0
            key=True
            found=False
            while key==True:

                if int(inp[1])<1:
                    key=False

                if int(inp[1])>fib(index):
                    index+=1

                if int(inp[1])<fib(index):
                    key=False

                if int(inp[1])==fib(index):
                    found=True
                    key=False
            if found==False:
                print("Number not found")

            if found==True:
                print(str(inp[1])+ " was found in the sequence")
        else:
            print("Invalid input")

if __name__ == "__main__":
  main()
            

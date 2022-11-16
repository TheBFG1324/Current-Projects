'''
Cameron Denton
lab3 exercise 1
Date: 9/26/22
last Mod: 9/26/22
Purpose: To get a base and a power and do the calculations using recursion
'''
#Exercise1.py
def power(a,b):
    cont=True
    if b<0:
        return "Invalid input"
        cont=False
    if b==0:
        return 1
    if cont==True:
        return a*power(a,b-1)


def main():
    keep=True
    while keep==True:
        base=int(input("Enter base: "))
        to=int(input("Enter power: "))
        print(power(base, to))
        keepgoing=input("Keep going? y/n: ")
        if keepgoing=="n":
            keep=False
        else:
            continue

if __name__ == "__main__":
  main()

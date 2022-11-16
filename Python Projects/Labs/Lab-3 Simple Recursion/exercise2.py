'''
Cameron Denton
lab3 exercise 2
Date: 9/26/22
last Mod: 9/26/22
Purpose: to do calculations useing recursion with a zombie outbreak case
'''
#exercise2

def sick(a):
    if a<1:
        return "Invalid Day"
    
    elif a==1:
        return 6
    elif a==2:
        return 20
    elif a==3:
        return 75
    
    return sick(a-1)+sick(a-2)+sick(a-3)

def main():
    key=True
    while key==True:
        day=int(input("Enter day for sick count: "))
        print(sick(day))
        keepgoing=input("Keep going? y/n: ")
        if keepgoing=="n":
            key=False
        else:
            continue

if __name__ == "__main__":
  main()
    

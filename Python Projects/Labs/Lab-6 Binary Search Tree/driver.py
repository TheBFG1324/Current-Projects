from binarysearchtree import BinarySearchTree
from executive import Executive
from poke import Poke


def main():
    inp = input("Enter input file: ")
    i = Executive(inp)
    x = BinarySearchTree()
    for pokemon in i.poke_matrix:
        x.add(pokemon)
    has_copied = False
    key = True
    while key == True:

        print("1)Search\n 2)Add\n 3)Print\n 4)Remove\n 5)Hard Copy\n 6)Quit")
        try:
            option = int(input("Enter Option: "))
            if option == 1:
                _search = int(input("Enter id: "))
                p = int(input("1) Main Tree 2) Copy Tree\n Enter option: "))
                if p == 1:
                    print(x.search(_search))
                elif p == 2:
                    if has_copied == True:
                        print(copy.search(_search))
                    else:
                        print("Copy has not been made yet")
                else:
                    print("Invalid entry")

            elif option == 2:
                _list = []
                name = input("Enter name: ")
                _list.append(name)
                _id = input("Enter id: ")
                _list.append(_id)
                j_name = input("Enter Japanese name: ")
                _list.append(j_name)
                new_poke = Poke(_list)
                p = int(input("1) Main Tree 2) Copy Tree\n Enter option: "))
                if p == 1:
                    x.add(new_poke)

                elif p == 2:
                    if has_copied == True:
                        copy.add(new_poke)

                    else:
                        print("Copy has not been made yet")
                else:
                    print("Invalid Entry")

            elif option == 3:
                which = int(input("(1) Print from main Search Tree 2)Print from copy\n Enter Choice: "))
                print("1)Pre Order\n 2)In Order\n 3)Post Order")
                op = int(input("Enter Traversal option number: "))
                if op == 1:
                    if which == 1:
                        x.preOrder()
                    elif which == 2:
                        if has_copied == True:
                            copy.preOrder()
                        else:
                            print("Copy has not been made yet")
                    else:
                        print("Invalid Entry")
                elif op == 2:
                    if which == 1:
                        x.inOrder()
                    elif which == 2:
                        if has_copied == True:
                            copy.inOrder()
                        else:
                            print("Copy has not been made yet")
                    else:
                        print("Invalid Entry")

                elif op == 3:
                    if which == 1:
                        x.postOrder()
                    elif which == 2:
                        if has_copied == True:
                            copy.postOrder()
                        else:
                            print("Copy has not been made yet")
                    else:
                        print("Invalid Entry")

                else:
                    print("Invalid Entry")
            elif option == 4:
                s = int(input("1)Remove from main Search Tree 2)Remove from copy\n Enter Choice: "))
                _id = int(input("Enter ID number to Remove: "))
                if s == 1:
                    x.remove(_id)
                elif s == 2:
                    if has_copied == True:

                        copy.remove(_id)
                    else:
                        print("Copy has not been made yet")

                else:
                    print("Invalid option")
            elif option == 5:
                if has_copied == False:
                    copy = x.copy()
                    has_copied = True

                else:
                    print("Copy has already been made")

            elif option == 6:
                key = False

            else:
                print("Invalid entry, try again")
        except:
            print("Invalid Entry, Try Again")


if __name__ == "__main__":
    main()

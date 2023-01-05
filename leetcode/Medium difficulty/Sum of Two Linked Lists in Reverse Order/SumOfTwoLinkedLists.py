from linkedlistleetcode import LinkedList

class Solution():
    def addTwoNumbers(self, l1, l2):
        length1=l1.length() #gets length of first linked list
        length2=l2.length() #gets length of second linked list

        number_one=[] #sets a variable that creates a list of values from the linked list
        for x in range(length1):
            value=l1.get_entry(x)
            number_one.append(value)
        
        number_one=number_one[::-1] #reverses the order of the list to the correct order

        print(number_one)

        number_two=[] #sets a variable that creates a list of values from the linked list
        for x in range(length2):
            value=l2.get_entry(x)
            number_two.append(value)
        
        number_two=number_two[::-1] #reverses the order of the list to the correct order

        
        
        
        number_one=list(map(str, number_one))
        number_two=list(map(str, number_two))


        number_one="".join(number_one) #joins ints in list to one integer value
        number_two="".join(number_two) #joins ints in list to one integer value

        final_ans=str(int(number_one) + int(number_two)) #adds two values
        final_ans=final_ans[::-1] #reverses it to the correct order
        final_linkedlist=LinkedList() #creates a linked list instance
        for x in range(len(final_ans)):
            final_linkedlist.insert(x, final_ans[x]) #adds each value to the linked list object
        
        return final_linkedlist #returns linked list

linked_list1=LinkedList()
linked_list1.insert(0, 1)
linked_list1.insert(1, 2)
linked_list1.insert(2, 3)
linked_list1.insert(3, 4)


linked_list2=LinkedList()
linked_list2.insert(0, 5)
linked_list2.insert(1, 6)
linked_list2.insert(2, 7)
linked_list2.insert(3, 8)

solution=Solution()

sol=solution.addTwoNumbers(linked_list1, linked_list2)

for x in range(sol.length()):
    print(sol.get_entry(x))

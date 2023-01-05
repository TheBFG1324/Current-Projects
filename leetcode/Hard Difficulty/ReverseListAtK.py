# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseGroupAtK(self, head, k):
        jumper=head
        for x in range(k):
            jumper=jumper.next
        
        connection=jumper
        before=None
        current=head
        while current!=connection:
           next_node=current.next
           current.next=before
           before=current
           current=next_node
        
        head=before
        jumper=head
        while jumper.next!=None:
            jumper=jumper.next
        jumper.next=connection

        return head

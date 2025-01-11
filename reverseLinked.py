# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None #keep track of the previous
        curr = head #keep track of the head

        while curr:
            temp = curr.next #store the next node
            curr.next = prev #reverse the linkedlist
            prev = curr #move curr forward
            curr = temp #move prev forward
        return prev
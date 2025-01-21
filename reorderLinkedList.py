class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def reorderLinkedList(head):
        '''
        First Split the list into two halves
        Reverse the second half
        Reorder them by pairing alternate nodes
        '''

        #check for single or empty lists
        if not head or not head.next:
            return
        
        #find the center of the linkedlist
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        #Reverse the second half of the linkedlist
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        #merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
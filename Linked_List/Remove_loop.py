# Given the head of a linked list that may contain a loop.  A loop means that the last node of the linked list is connected back to a node in the same list. The task is to remove the loop from the linked list (if it exists).

# Custom Input format:

# A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.

# The generated output will be true if there is no loop in list and other nodes in the list remain unchanged, otherwise, false.

class Solution:
    def removeLoop(self, head):
        if not head or head.next is None:
            return False
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return False
        
        slow = head
        #Checking if fast is pointing to start of the list
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
        else:
            #If not start then move 1 step at a time and continue till they meet again and then remoove pointer of fast.next to None
            while slow.next != fast.next:
                slow=slow.next
                fast=fast.next
        
        fast.next=None
        return True
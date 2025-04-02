class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        if head==None:
            return None
        slow=head
        fast=head
        while(fast.next is not None and fast.next.next is not None):
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False        
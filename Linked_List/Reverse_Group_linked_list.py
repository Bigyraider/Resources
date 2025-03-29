#Given the head a linked list, the task is to reverse every k node in the linked list. 
# If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        counter=0
        curr, prev=head, None
        while counter<k and curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            counter+=1
        if curr:
            head.next = self.reverseKGroup(curr,k)
        
        return prev
from collections import deque
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def reverseLevelOrder(self,root):
        # code here
        res=[]
        queue=deque([root])
        
        while queue:
            current=queue.popleft()
            res.append(current.data)
            
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return res[::-1]
from collections import deque
"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        if not root:
            return []
        
        result = []
        queue=deque([root])    #Adding root to the queue
        
        while queue:
            level_size=len(queue)               
            level_nodes=[]                  #Maintain level wise nodes in []
            
            for _ in range(level_size):
                current=queue.popleft()                    #pop left most element ex- [root,1] so root will be poped
                level_nodes.append(current.data)           # add value to the level_nodes and then to stack 
                
                if current.left:
                    queue.append(current.left)             #Check if that current node has left and right element
                if current.right:
                    queue.append(current.right)
            
            result.append(level_nodes)                     
        return result
    
# [[1], [2, 3]] - output

# Time complexity - O(N)
# Space complexity - O(N)
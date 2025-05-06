# class Node:
#     def _init_(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
# '''
# # your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return None
        
        root.left, root.right = self.mirror(root.right),self.mirror(root.left)
        return root
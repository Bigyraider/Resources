# Given a binary tree, find its height.

# The height of a tree is defined as the number of edges on the longest path from the root to a leaf node. A leaf node is a node that does not have any children.

def height(self, root):
    # code here
    if root is None:
        return -1
    
    left_height = self.height(root.left)
    right_height = self.height(root.right)
    
    if left_height>right_height:
        return 1+left_height
    else: 
        return 1+right_height
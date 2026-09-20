# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            root = TreeNode(val)
            return root
        
        curr = root

        while curr:
            curr_value = curr.val

            if val > curr_value:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right
            else:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
        
        return root

            
        
        

        
        
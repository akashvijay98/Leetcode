# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
            
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root,float('-inf'),float('inf'))
    
    def dfs(self,root,low,high):
        if root==None:
            return True
        
        elif root.val<=low or root.val>=high:
            return False
        
        
        else:
            return self.dfs(root.left,low,root.val) and self.dfs(root.right,root.val,high)
            
            
            

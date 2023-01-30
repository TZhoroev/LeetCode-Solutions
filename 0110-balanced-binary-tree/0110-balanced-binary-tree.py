# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: 
                return 0
            l_length = dfs(node.left)
            if l_length == -1: return -1
            r_length = dfs(node.right)
            if r_length == -1: return -1
            if abs(l_length - r_length) > 1:
                return -1
            else:
                return max(l_length, r_length) + 1
        return True if dfs(root) != -1 else False
            
        
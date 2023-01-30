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
                return True, 0
            l_cond, l_length = dfs(node.left)
            r_cond, r_length = dfs(node.right)
            if abs(l_length - r_length) > 1:
                return False, max(l_length, r_length)
            else:
                return l_cond and r_cond, max(l_length, r_length) + 1
        return dfs(root)[0]
            
        
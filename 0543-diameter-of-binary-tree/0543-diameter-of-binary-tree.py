# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(root):
            if root is None: return 0
            l_length = dfs(root.left)
            r_length = dfs(root.right)
            self.diameter = max(self.diameter, l_length + r_length)
            return max(l_length, r_length) + 1 
        dfs(root)
        return self.diameter
    
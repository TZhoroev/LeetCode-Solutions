# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = - float("inf")
        def dfs(root, p_sum):
            if root is None: return  - float("inf")
            l_sum = dfs(root.left, p_sum + root.val)
            r_sum = dfs(root.right, p_sum + root.val)
            c_max = max(l_sum, r_sum, 0) + root.val
            self.max = max(self.max, c_max, l_sum + r_sum + root.val)
            return c_max
        dfs(root, 0)
        return self.max

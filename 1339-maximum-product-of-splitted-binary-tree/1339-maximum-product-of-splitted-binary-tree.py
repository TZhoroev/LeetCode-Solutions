# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def dfs_total(root):
            if root is None: return 0
            return dfs_total(root.left) + dfs_total(root.right) + root.val
        total = dfs_total(root)
        def dfs_sub(root):
            if root is None: return 0
            c_sum = dfs_sub(root.left) + dfs_sub(root.right) + root.val
            self.max = max(self.max, (total - c_sum)*c_sum)
            return c_sum
        dfs_sub(root)
        return self.max % (10 ** 9 + 7)
            
        
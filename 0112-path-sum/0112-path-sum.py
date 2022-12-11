# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, p_sum):
            if root is None: return False
            if root.left is None and root.right is None:
                return p_sum + root.val == targetSum
            return dfs(root.left, p_sum + root.val) or dfs(root.right, p_sum + root.val)
        return dfs(root, 0)

        
        
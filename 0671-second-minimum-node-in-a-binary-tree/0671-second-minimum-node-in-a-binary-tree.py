# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        secondmin = float("inf")
        stack = [root]
        while stack:
            node = stack.pop()
            # If node.val> secondmin, then so do child nodes. 
            if node.val < secondmin and node.left:
                stack.append(node.left)
                stack.append(node.right)
            if root.val < node.val < secondmin:
                secondmin = node.val
        return secondmin if secondmin != float("inf") else -1
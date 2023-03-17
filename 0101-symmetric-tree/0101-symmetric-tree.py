# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or ( not root.left and not root.right): return True
        stack = [(root.left, root.right)]
        while stack:
            left_h, right_h = stack.pop()
            if not left_h and not right_h: continue
            elif not left_h or not right_h or left_h.val != right_h.val: return False
            stack.append((left_h.left, right_h.right))
            stack.append((left_h.right, right_h.left))
        return True
            
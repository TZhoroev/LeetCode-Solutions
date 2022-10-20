# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        stack_p, stack_q = [p], [q]
        while stack_p and stack_q:
            a, b = stack_p.pop(), stack_q.pop()
            if a.val != b.val: return False
            if a.left and b.left: stack_p.append(a.left), stack_q.append(b.left)
            elif a.left or b.left:return False
            if a.right and b.right: stack_p.append(a.right), stack_q.append(b.right)
            elif a.right or b.right:return False
        return True
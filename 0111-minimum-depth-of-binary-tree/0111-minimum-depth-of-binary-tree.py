# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        Q = deque()
        Q.append([root, 0])
        while Q:
            node, depth = Q.popleft()
            if not node.left and not node.right:
                return depth + 1
            if node.left:
                Q.append([node.left, depth + 1])
            if node.right:
                Q.append([node.right, depth + 1])
        
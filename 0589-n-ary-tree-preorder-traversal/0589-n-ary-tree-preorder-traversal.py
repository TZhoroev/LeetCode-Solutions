"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result =[]
        if not root: return result
        stack = [root]
        while stack:
            current_node = stack.pop()
            result.append(current_node.val)
            stack.extend(current_node.children[::-1])
        return result
        
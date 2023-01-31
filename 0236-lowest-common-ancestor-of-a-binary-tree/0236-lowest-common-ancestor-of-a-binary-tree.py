# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        ans = -1
        def dfs(node):
            nonlocal ans
            if not node:
                return -1
            left, right = dfs(node.left), dfs(node.right)
            current = (node.val == p.val or node.val == q.val)
            print(node.val, left, right, current)
            if current:
                if left == 0 or right == 0:
                    ans = node
                    return 1
                
                return 0
            else:
                if (left == 0 and right == 0):
                    ans = node
                    return 1
                elif left == 1 or right == 1:
                    return 1
                elif left == 0 or right == 0:
                    return 0
                else:
                    return -1

            
        dfs(root)
        return ans
    
        
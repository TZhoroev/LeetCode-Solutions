# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def inorder(root,nums):
            if root is None:
                return
            inorder(root.left,nums)
            nums.append(root.val) 
            inorder(root.right,nums)
        
        nums = []
        inorder(root,nums)
        ans = []
        n = len(nums)
        for q in queries:
            i = bisect_left(nums,q)
            if i == n:
                temp = ([nums[i-1],-1])
            elif nums[i] == q:
                temp = ([q,q])
            elif i == 0:
                temp = ([-1,nums[i]])
            else:
                temp = ([nums[i-1],nums[i]])
            ans.append(temp)
            
        return ans
        
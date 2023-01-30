# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createBST(left, right):
            if right < left: return None
            mid = math.ceil((left + right) / 2)
            current = TreeNode(nums[mid])
            current.left = createBST(left, mid - 1)
            current.right = createBST(mid + 1, right)
            return current
        return createBST(0, len(nums) - 1)
        
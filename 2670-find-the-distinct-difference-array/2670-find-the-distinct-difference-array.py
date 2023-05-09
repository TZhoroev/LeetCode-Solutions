class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        elements, unique = set(), [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums) - 1, -1, -1):
            elements.add(nums[i])
            unique[i] = len(elements)
        elements = set()
        results = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            elements.add(nums[i])
            results[i] = len(elements) - unique[i + 1]
        return results
        
        
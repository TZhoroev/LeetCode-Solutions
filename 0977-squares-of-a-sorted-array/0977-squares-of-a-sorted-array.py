class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans, abs_min = [], float("inf")
        for index, num in enumerate(nums):
            if abs(num) <= abs_min:
                abs_min = abs(num)
                i = index
            else:
                break
        j = i + 1
        while i >= 0 or j < len(nums):
            if i >= 0 and j < len(nums):
                if abs(nums[i]) <= abs(nums[j]):
                    ans.append(nums[i] ** 2)
                    i -= 1
                else:
                    ans.append(nums[j] ** 2)
                    j += 1
            elif i >= 0:
                ans.append(nums[i] ** 2)
                i -= 1
            elif j < len(nums):
                ans.append(nums[j] ** 2)
                j += 1
        return ans
      
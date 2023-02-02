class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n = [], len(nums)
        def dfs(nums, path):
            if len(path) == n: ans.append(path)
            for i in range(len(nums)):
                if i and nums[i] == nums[i -1]:
                    continue
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        return ans
        
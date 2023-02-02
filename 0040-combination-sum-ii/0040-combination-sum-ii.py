class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, ans = len(nums), []
        def dfs(nums, target, path):
            if target < 0:
                return
            elif target == 0:
                ans.append(path)
                return
            for i in range(len(nums)):
                if i and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[i+1:], target - nums[i], path + [nums[i]])
        dfs(nums, target, [])
        return ans
        
        
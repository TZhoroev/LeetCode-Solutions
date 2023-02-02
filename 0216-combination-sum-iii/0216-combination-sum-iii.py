class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums, ans = [i for i in range(1, 10)], []
        def dfs(nums, target, path):
            if len(path) > k or target < 0:
                return
            elif len(path) == k and target == 0:
                ans.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], target - nums[i], path + [nums[i]])
        dfs(nums, n, [])
        return ans
        
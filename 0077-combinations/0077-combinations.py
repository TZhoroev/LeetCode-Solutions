class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        ans = []
        def dfs(nums, path):
            if len(path) == k:
                ans.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i + 1:], path+[nums[i]])
        dfs(nums, [])
        return ans
        
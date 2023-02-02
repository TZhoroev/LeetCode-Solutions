class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []
        def dfs(nums, path):
            if len(path)== n:
                ans.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path +[nums[i]])
        dfs(nums, [])
        return ans
        
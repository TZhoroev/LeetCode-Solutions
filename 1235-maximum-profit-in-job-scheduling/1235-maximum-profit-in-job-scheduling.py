class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        @cache
        def dfs(idx):
            if idx >=len(jobs): return 0
            next_idx = bisect_left(jobs, jobs[idx][1], key = lambda job: job[0])
            return max(dfs(idx + 1), jobs[idx][2] + dfs(next_idx))
        return dfs(0)
        
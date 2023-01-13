class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g, ans = [[] for _ in range(len(s))], 1
        for index, node in enumerate(parent):
            if index != 0: g[node].append(index)
                
        def dfs(node, res = 1):
            if not g[node]: return 1
            nonlocal ans
            for v in g[node]:
                c_res = dfs(v)
                if s[node] != s[v]:
                    ans, res = max(ans, c_res + res), max(res, c_res + 1)
            return res
        
        dfs(0)
        return ans
        
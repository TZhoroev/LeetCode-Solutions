from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for _ in range(len(roads) + 1)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        @cache
        def dfs(v, par):
            cost, people = 0, 1
            for u in graph[v]:
                if u != par:
                    c, p = dfs(u, v)
                    cost += c + ceil(p / seats)
                    people += p
            return cost, people
        ans, _ = dfs(0, -1)
        return ans
                
                
            
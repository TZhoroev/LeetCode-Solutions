class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        seen = [False] * n
        count = [0] * 26
        ans = [0] * n
        def postOrder(i):
            if seen[i]: return
            seen[i] = True
            before = count[ord(labels[i]) - ord('a')]
            for j in g[i]: postOrder(j)
            count[ord(labels[i]) - ord('a')] += 1
            ans[i] = count[ord(labels[i]) - ord('a')] - before
        postOrder(0)
        return ans
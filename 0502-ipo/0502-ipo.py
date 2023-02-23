class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [[p, c] for p, c in zip(profits, capital)]
        pairs.sort(key = lambda x:x[1])
        i = 0
        n = len(capital)
        pq = []
        while k > 0:
            while i < n and pairs[i][1] <= w:
                heappush(pq, -pairs[i][0])
                i += 1
            if not pq:
                break
            w -= heappop(pq)
            k -= 1
        return w
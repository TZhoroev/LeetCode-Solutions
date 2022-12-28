class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles[:], total = [-x  for x in piles], sum(piles)
        heapify(piles)
        while piles and k:
            current = - heappop(piles)
            total -= current // 2
            k -= 1
            heappush(piles, - current //2 )
        return total
            
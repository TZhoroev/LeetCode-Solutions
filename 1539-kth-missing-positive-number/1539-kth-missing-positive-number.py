class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr = set(arr)
        count = 0
        for i in range(1, n + k):
            if i not in arr:
                count += 1
                if count == k:
                    return i
        return n + k
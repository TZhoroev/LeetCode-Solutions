from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(lambda: -1)
        for index, item in enumerate(nums):
            idx = d[item]
            if idx != -1 and index - idx <= k:
                return True
            d[item] = index
        return False
        
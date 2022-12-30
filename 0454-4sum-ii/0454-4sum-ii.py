class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        targets = defaultdict(lambda: 0)
        for num1 in nums1:
            for num2 in nums2:
                targets[num1+num2] += 1
        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                ans += targets[-(num3 + num4)]
        return ans
        
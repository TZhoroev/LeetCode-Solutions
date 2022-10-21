class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m, i, j = len(nums1), len(nums2), 0, 0
        k, a, b = (n+ m + 1)//2, -float("inf"), -float("inf")
        nums1.append(float("inf")), nums2.append(float("inf"))
        while i <= n and j <= m:
            if nums1[i] <= nums2[j]:
                a, b = b, nums1[i]
                i += 1
            else:
                a, b = b, nums2[j]
                j += 1
            if i + j - 1== k:
                if (n+m)%2==0: return (a + b)/2
                else: return float(a)
            
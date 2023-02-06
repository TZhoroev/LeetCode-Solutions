class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res, i, index = [0 for _ in range(2*n)], 0, 0
        while i < n:
            res[index], res[index + 1] = nums[i], nums[i + n]
            i += 1; index += 2
        return res
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        res, i = [0 for _ in range(len(nums))], 0
        while nums:
            res[i] = heappop(nums)
            i +=1
        return res
        
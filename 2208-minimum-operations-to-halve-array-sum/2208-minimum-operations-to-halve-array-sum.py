class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # heapq is used for minheap, so change all numbers to negative of it to use 
        # as  max heap
        nums[:] = [- x for x in nums]
        total = sum(nums)
        half_sum = total
        heapq.heapify(nums)
        step = 0
        while half_sum < total/2:
            x = heapq.heappop(nums)
            half_sum -= x/2
            heapq.heappush(nums, x/2)
            step += 1
        return step
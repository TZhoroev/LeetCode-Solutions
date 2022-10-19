class Solution:
    def jump(self, nums: List[int]) -> int:
        count, distance, position  = 0, 0, 0
        for index in range(len(nums) -1):
            distance = max(index+nums[index], distance)
            if index == position:
                position = distance
                count +=1
        return count
        
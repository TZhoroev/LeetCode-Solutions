class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[right] > nums[mid]: 
                if nums[right] >= target > nums[mid]: 
                    left = mid + 1
                else: right = mid - 1
            else: # if it's rotated form
                if nums[left]<= target < nums[mid]: # if the target is in left half
                    right = mid - 1
                else: left = mid + 1 # if the target is in right half
        return -1
        
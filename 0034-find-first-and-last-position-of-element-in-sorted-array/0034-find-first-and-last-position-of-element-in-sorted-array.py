class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.b_search_left(nums, target)
        return [-1, -1] if left == -1 else [left, self.b_search_right(nums, target)]
            
    
    

    def b_search_right(self, keys, query):
        min_index = 0
        max_index = len(keys) - 1
        while max_index >= min_index:
            mid_index = (max_index + min_index) // 2
            if keys[mid_index] == query and (mid_index == max_index or query< keys[mid_index + 1]):
                return mid_index
            elif keys[mid_index] > query:
                max_index = mid_index - 1
            else:
                min_index = mid_index + 1
        return -1
    
    def b_search_left(self, keys, query):
        min_index = 0
        max_index = len(keys) - 1
        while max_index >= min_index:
            mid_index = (max_index + min_index) // 2
            if keys[mid_index] == query and (mid_index == min_index or query > keys[mid_index - 1]):
                return mid_index
            elif keys[mid_index] < query:
                min_index = mid_index + 1
            else:
                max_index = mid_index - 1
        return -1
        
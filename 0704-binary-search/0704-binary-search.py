class Solution:
    def search(self, keys: List[int], query: int) -> int:
        min_index = 0
        max_index = len(keys) - 1
        while max_index >= min_index:
            mid_index = (max_index + min_index) // 2
            if keys[mid_index] == query:
                return mid_index
            elif keys[mid_index] < query:
                min_index = mid_index + 1
            else:
                max_index = mid_index - 1
        return -1
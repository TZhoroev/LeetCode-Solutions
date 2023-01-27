class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)< 3: return 0
        right_max, c_max = [height[-1] for _ in range(len(height) - 1) ], height[-1]
        for i in range(len(height) - 2, 0, -1):
            if height[i] > c_max:
                c_max = height[i]
            right_max[i - 1] = c_max
        left_max = height[0] 
        res = 0
        for i  in range(1, len(height) - 1):
            if height[i] < min(left_max, right_max[i]):
                res += min(left_max, right_max[i]) - height[i]
            elif height[i] > left_max:
                left_max = height[i]
        return res


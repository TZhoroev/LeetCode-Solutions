class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        next_smallest = [len(arr) for _ in range(len(arr))]
        prev_smallest = [-1 for _ in range(len(arr))]
        inc_stack = []
        
        for i in range(len(arr)):
            while len(inc_stack) > 0 and arr[inc_stack[-1]] >= arr[i]:
                next_smallest[inc_stack.pop()] = i
                
            if len(inc_stack) > 0:
                prev_smallest[i] = inc_stack[-1]
            inc_stack.append(i)
    
        s = 0
        for i in range(len(arr)):
            
            s += (i - prev_smallest[i]) * (next_smallest[i] - i) * arr[i]
        
        return s % (10 ** 9 + 7)
        
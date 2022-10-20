class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        integers = set()
        for num in nums:
            integers.add(num)
            integers.add(int(str(num)[::-1]))
        return len(integers)
        
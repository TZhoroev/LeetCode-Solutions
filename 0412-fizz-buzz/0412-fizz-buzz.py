class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 and i % 5:
                ans.append(str(i))
            elif i % 3:
                ans.append("Buzz")
            elif i % 5:
                ans.append("Fizz")
            else:
                ans.append("FizzBuzz")
        return ans
        
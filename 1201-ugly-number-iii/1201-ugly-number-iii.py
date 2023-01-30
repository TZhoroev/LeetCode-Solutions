class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left, right = 1, 2 * (10 ** 9)
        ab, ac, bc, abc = math.lcm(a, b), math.lcm(a, c), math.lcm(b, c), math.lcm(a, b, c)
        def helper(p):
            count = p // a + p // b + p // c
            count -= (p // ab + p // ac + p // bc)
            count += p // abc
            print(p, count)
            return count >= n
        ans = -1 
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                right, ans = mid - 1, mid
            else:
                left = mid + 1
        return ans
        
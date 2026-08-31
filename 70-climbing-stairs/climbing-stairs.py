from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def f(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            return f(i-1) + f(i-2)
        return f(n)

        
# -*- coding: utf-8 -*-
"""
2025.03.06  19:02
by otto
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True

        while True:
            if n == 3:
                break
            if n % 3 != 0:
                return False
            n = n//3

        return True

solution = Solution()
ans = solution.isPowerOfThree(27)
print(ans)
# -*- coding: utf-8 -*-
"""
2025.03.06  18:58
by otto
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        while True:
            if n == 2:
                break
            elif n % 2 != 0:
                return False
            n = n // 2

        return True

solution = Solution()
ans = solution.isPowerOfTwo(8)
print(ans)

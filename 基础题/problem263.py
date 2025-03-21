# -*- coding: utf-8 -*-
"""
2025.03.06  19:38
by otto
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        while n%2 == 0:
            n = n//2
        while n%3 == 0:
            n = n//3
        while n%5 == 0:
            n = n//5
        if n == 1:
            return True
        else:
            return False
s = Solution()
print(s.isUgly(18))
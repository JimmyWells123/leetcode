# -*- coding: utf-8 -*-
"""
2025.03.06  20:05
by otto
"""

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[matrix[j][i] for j in range(m)] for i in range(n)]
        return ans

s = Solution()
ans = s.transpose([[1,2,3],[4,5,6],[7,8,9]])
print(ans)

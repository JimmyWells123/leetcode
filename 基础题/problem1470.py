# -*- coding: utf-8 -*-
"""
2025.03.06  19:50
by otto
"""
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
s = Solution()
ans = s.shuffle([1,1,2,2], 2)
print(ans)

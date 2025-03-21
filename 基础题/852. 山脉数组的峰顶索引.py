# -*- coding: utf-8 -*-
"""
2025.03.06  21:29
by otto
"""
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx = len(arr)//2
        start = 0
        end = len(arr)-1
        while True:
            if arr[idx] > arr[idx-1]:
                if arr[idx] > arr[idx+1]:
                    return idx
                start = idx
            else:
                end = idx
            idx = (start + end) // 2
set()

s = Solution()
print(s.peakIndexInMountainArray([0,10,5,2]))
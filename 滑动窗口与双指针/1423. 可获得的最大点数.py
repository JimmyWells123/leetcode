# -*- coding: utf-8 -*-
"""
2025.03.21  17:36
by otto
"""
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        n_left = n - k
        sum_all = sum(cardPoints)
        if n == k:
            return sum_all
        min_sub = 1e9
        sum_sub = 0

        for i in range(n):
            sum_sub += cardPoints[i]

            if i < n_left-1:
                continue

            min_sub = min(min_sub, sum_sub)

            sum_sub -= cardPoints[i-n_left+1]

        return sum_all - min_sub

if __name__ == '__main__':
    s = Solution()
    print(s.maxScore([9,7,7,9,7,7,9], 7))

# -*- coding: utf-8 -*-
"""
2025.03.06  20:44
by otto
"""
class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            left, right = s[:i], s[i+1:]
            print(left, right)
            for charater in left:
                if charater == '0':
                    score += 1
            for charater in right:
                if charater == '1':
                    score += 1
        return score
s = 'abcd'
left, right = s[:4], s[4:]
print(left, right)
# -*- coding: utf-8 -*-
"""
2025.03.06  23:06
by otto
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = n_vowels =0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                n_vowels += 1
            if i < k-1:
                continue
            max_vowels = max(max_vowels, n_vowels)
            if s[i-k+1] in 'aeiou':
                n_vowels -= 1
        return max_vowels
s = Solution()
print(s.maxVowels('weallloveyou', 7))

# -*- coding: utf-8 -*-
"""
2025.06.05  23:21
by otto
"""
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def
            max_len = sub_len = 0
            right = -1
            n = len(answerKey)
            repeated_count = 0

            for left in range(n):
                if left != 0:
                    if
# -*- coding: utf-8 -*-
"""
2025.03.21  18:28
by otto
"""
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        if k > 0:
            code_new = [0] * n
            for i in range(n):
                sub_sum = 0
                for j in range(1, k+1):
                    sub_sum += code[(i+j) % n]
                code_new[i] = sub_sum

            return code_new

        if k < 0:
            code_new = [0] * n
            for i in range(n):
                sub_sum = 0
                for j in range(1, abs(k) + 1):
                    sub_sum += code[(i - j) % n]
                code_new[i] = sub_sum

            return code_new
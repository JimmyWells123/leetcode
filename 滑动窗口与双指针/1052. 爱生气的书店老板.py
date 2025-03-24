# -*- coding: utf-8 -*-
"""
2025.03.21  18:03
by otto
"""
from typing import List
import numpy as np
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        original = int(np.dot(np.array(customers) , np.array(grumpy)*-1 + 1))
        add_max = sub_sati = 0
        n = len(customers)
        for i in range(n):

            sub_sati += customers[i] * grumpy[i]

            if i < minutes - 1:
                continue

            add_max = max(add_max, sub_sati)


            sub_sati -= customers[i-minutes+1] * grumpy[i-minutes+1]

        return original + add_max
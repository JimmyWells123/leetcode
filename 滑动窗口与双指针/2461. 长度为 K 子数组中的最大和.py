# -*- coding: utf-8 -*-
"""
2025.03.21  17:23
by otto
"""
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = sub_sum = 0
        sub_dict = {}
        n = len(nums)
        for i in range(n):
            sub_sum += nums[i]
            if nums[i] not in sub_dict:
                sub_dict[nums[i]] = 1
            else:
                sub_dict[nums[i]] += 1

            if i < k-1:
                continue

            if len(sub_dict) == k:
                max_sum = max(max_sum, sub_sum)

            # 滑出时操作
            sub_sum -= nums[i-k+1]
            if sub_dict[nums[i-k+1]] == 1:
                sub_dict.pop(nums[i-k+1])
            else:
                sub_dict[nums[i-k+1]] -= 1

        return max_sum
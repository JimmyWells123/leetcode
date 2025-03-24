# -*- coding: utf-8 -*-
"""
2025.03.21  16:10
by otto
"""
from typing import List
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        max_sum = sub_sum = 0
        n = len(nums)
        sub_dict = {}
        for i in range(n):
            sub_sum += nums[i]
            if nums[i] not in sub_dict:
                sub_dict[nums[i]] = 1
            else:
                sub_dict[nums[i]] += 1
            if i < k-1:
                continue
            if len(sub_dict) >= m:
                max_sum = max(max_sum, sub_sum)

            # 滑出时的操作
            if sub_dict[nums[i-k+1]] == 1:
                sub_dict.pop(nums[i-k+1])
            else:
                sub_dict[nums[i-k+1]] -= 1

            sub_sum -= nums[i-k+1]

        return max_sum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSum([1,2,2], 2, 2))
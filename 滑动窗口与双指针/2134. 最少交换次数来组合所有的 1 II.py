from typing import List
class Solution:
    def minSawps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        nums = nums * 2
        max_ones = ones = 0
        for i in range(2*n):
            ones += nums[i]

            if i < k-1:
                continue
            max_ones = max(max_ones, ones)
            ones -= nums[i-k+1]
        return k - max_ones
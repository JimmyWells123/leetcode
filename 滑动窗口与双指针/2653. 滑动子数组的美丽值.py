from typing import List
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        sorted_sub_list = nums[:k]
        sorted_sub_list.sort()
        res = [min(0, sorted_sub_list[x-1])]
        for i in range(k, n):
            sorted_sub_list.remove(nums[i-k])
            for j in range(k-1):
                if sorted_sub_list[j] >= nums[i]:
                    sorted_sub_list.insert(j, nums[i])
                    break
            else:
                sorted_sub_list.append(nums[i])
            res.append(min(0, sorted_sub_list[x-1]))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.getSubarrayBeauty([-3,1,2,-3,0,-3], 2, 1))  # [2,3,4]
            

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        right_idx = -1
        sub_s_set = set()
        for i in range(n):
            if i != 0:
                sub_s_set.remove(s[i-1])
            
            while right_idx + 1 < n and s[right_idx+1] not in sub_s_set:
                sub_s_set.add(s[right_idx+1])
                right_idx += 1

            max_length = max(right_idx - i +1, max_length)
        return max_length

if __name__ =="__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring('abb')
    print(res)

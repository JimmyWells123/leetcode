class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        right = -1
        sub_s_dict = {}
        for left in range(n):
            if left != 0:
                if sub_s_dict[s[left-1]] == 1:
                    sub_s_dict.pop(s[left-1])
                else:
                    sub_s_dict[s[left-1]] -= 1
            
            while right + 1 < n and (s[right+1] not in sub_s_dict or sub_s_dict[s[right+1]] < 2):
                if s[right + 1] not in sub_s_dict:
                    sub_s_dict[s[right + 1]] = 1
                else:
                    sub_s_dict[s[right + 1]] += 1
                
                right += 1
            
            max_length = max(right - left + 1, max_length)
            
        return max_length
if __name__ =="__main__":
    s = Solution()
    res = s.maximumLengthSubstring("aaab")
    print(res)

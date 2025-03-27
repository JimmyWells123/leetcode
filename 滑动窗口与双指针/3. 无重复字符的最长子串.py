class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        j = 0
        max_length = 0
        sub_string = ''
        while i < n and j < n:
            if s[j] not in sub_string:
                sub_string = s[i:j+1]
                max_length = max(j-i+1, max_length)
                j += 1

            else:
                i += 1
                sub_string = s[i:j]

        
        return max_length

if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring("aab")
    print(res)
            
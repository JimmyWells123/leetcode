from typing import List
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        substring_dict = {}
        k = minSize
        letters_dict ={}
        for i in range(n):
            if s[i] not in letters_dict:
                letters_dict[s[i]] = 1
            else:
                letters_dict[s[i]] += 1
            
            if i < k-1:
                continue

            if len(letters_dict) <= maxLetters:
                substring = s[i-k+1:i+1]
                if substring not in substring_dict:
                    substring_dict[substring] = 1
                else:
                    substring_dict[substring] += 1
            
            if letters_dict[s[i-k+1]] == 1:
                letters_dict.pop(s[i-k+1])
            else:
                letters_dict[s[i-k+1]] -= 1
        return max(substring_dict.values(), default=0)


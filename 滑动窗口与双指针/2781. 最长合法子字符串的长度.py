# -*- coding: utf-8 -*-
"""
2025.03.21  21:05
by otto
"""
from typing import List
# from test import lst, a

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        length_set_forbidden = set()
        for item in forbidden:
            length_set_forbidden.add(len(item))
        print(length_set_forbidden)

        n = len(word)
        max_valid_substring = 0
        i = 0
        j = 0
        while j < n:

            sub_string = word[i:j+1]
            n_sub = len(sub_string)

            for length in length_set_forbidden:
                if n_sub < length:
                    continue
                if sub_string[n_sub - length:] in forbidden:
                    i += 1
                    break
            else:
                max_valid_substring = max(max_valid_substring, n_sub)
                j += 1


        return max_valid_substring

if __name__ == '__main__':
    s = Solution()
    print(s.longestValidSubstring("cbaaaabc", ["aaa","cb"]))

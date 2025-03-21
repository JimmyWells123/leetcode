# -*- coding: utf-8 -*-
"""
2025.03.06  21:11
by otto
"""

left=0
right = 2
words = ["are","amy","u"]
ans = 0
for i in range(left, right+1):
    vow = ['a', 'e', 'i', 'o', 'u']
    print(words[i])
    if words[i][0] in vow and words[i][-1] in vow:
        ans += 1
print(ans)
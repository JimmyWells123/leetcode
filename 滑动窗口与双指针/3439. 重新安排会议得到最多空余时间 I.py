from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        intervals = []
        intervals.append(startTime[0])
        for i in range(1, n):
            intervals.append(startTime[i] - endTime[i-1])
        intervals.append(eventTime - endTime[-1])

        k += 1
        max_free_time = free_time = 0
        for i in range(n+1):
            free_time += intervals[i]

            if i < k-1:
                continue

            max_free_time = max(max_free_time, free_time)

            free_time -= intervals[i-k+1]
        return max_free_time

if __name__ == '__main__':
    s = Solution()
    print(s.maxFreeTime(21, 2, [18, 20], [20, 21]))  # 3

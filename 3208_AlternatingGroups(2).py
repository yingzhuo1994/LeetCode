# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        start = 0
        end = 0
        n = len(colors)
        while start < n:
            for end in range(start + 1, n * 2):
                i = (end - 1) % n
                j = end % n
                if colors[i] == colors[j]:
                    end -= 1
                    break
            diff = end - start + 1 - k + 1
            if diff > 0:
                ans += min(diff, n - start)
            start = end + 1
        return ans
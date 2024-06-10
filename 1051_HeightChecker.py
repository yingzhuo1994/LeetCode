# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i, num in enumerate(heights):
            if num != expected[i]:
                ans += 1
        return ans


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        max_val = max(heights)
        
        # Create frequency table
        freq = [0] * (max_val + 1)
        for num in heights: freq[num] += 1
        for num in range(1, len(freq)): freq[num] += freq[num-1]

        # Create places table
        places = [0] * len(heights)
        for num in heights:
            places[freq[num]-1] = num
            freq[num] -= 1

        return sum([a!=b for a, b in zip(heights, places)])
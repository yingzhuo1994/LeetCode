# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        memo = {}
        for row in matrix:
            key = "".join(map(str, row))
            memo[key] = memo.get(key, 0) + 1
        for key in memo:
            mask = "".join(["1" if ch == "0" else "0" for ch in key])
            count = memo.get(mask, 0) + memo[key]
            ans = max(ans, count)
        return ans


# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Dictionary to store frequency of each pattern
        pattern_frequency = {}

        for current_row in matrix:
            # Convert row to pattern using list comprehension and join
            # 'T' if element matches first element, 'F' otherwise
            row_pattern = "".join(
                "T" if num == current_row[0] else "F" for num in current_row
            )

            # Update pattern frequency using dict.get() with default value
            pattern_frequency[row_pattern] = (
                pattern_frequency.get(row_pattern, 0) + 1
            )

        # Return maximum frequency using max() with default of 0
        return max(pattern_frequency.values(), default=0)
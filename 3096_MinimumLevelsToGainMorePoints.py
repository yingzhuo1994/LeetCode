# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        scores = [0]
        for val in possible:
            if val == 1:
                scores.append(scores[-1] + 1)
            else:
                scores.append(scores[-1] - 1)
        for i in range(1, len(scores) - 1):
            if scores[i] > scores[-1] - scores[i]:
                return i
        return -1
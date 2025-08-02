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


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        total = sum([1 if val == 1 else -1 for val in possible])
        score = 0
        for i in range(len(possible) - 1):
            if possible[i] == 1:
                score += 1
            else:
                score -= 1
            if score > total - score:
                return i + 1
        return -1
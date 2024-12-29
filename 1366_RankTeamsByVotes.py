# 1st solution
# O(n * log(n)) time | O(n^2) space
from functools import cmp_to_key
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        scores = {}
        for vote in votes:
            for i, ch in enumerate(vote):
                if ch not in scores:
                    scores[ch] = [0 for _ in range(len(vote))]
                scores[ch][i] += 1
        def compare(a, b):
            for v1, v2 in zip(scores[a], scores[b]):
                if v1 > v2:
                    return -1
                elif v1 < v2:
                    return 1
            return -1 if a < b else 1
                
        ranks = list(scores.keys())
        ranks.sort(key=cmp_to_key(compare))
        return "".join(ranks)
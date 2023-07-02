# 1st solution
# O((n + r) * 2^r) time | O(n + r) space
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        total = len(requests)
        idxArray = [j for j in range(total)]
        for i in reversed(range(total + 1)):
            for c in itertools.combinations(idxArray, i):
                net = [0 for _ in range(n)]
                for idx in c:
                    net[requests[idx][0]] -= 1
                    net[requests[idx][1]] += 1
                if net == [0 for j in range(n)]:
                    return i
        return 0
# 1st solution
# O(n + k) time | O(n) space
# where n = len(arr) and k = len(queries)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for num in arr:
            prefix.append(num ^ prefix[-1])
        ans = [prefix[b + 1] ^ prefix[a] for a, b in queries]
        return ans
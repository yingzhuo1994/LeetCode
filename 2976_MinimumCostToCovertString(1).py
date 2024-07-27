# 1st solution
# O(n + 26^3) time | O(26^2)
# where n = len(source)
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dic = {}
        alphabet = string.ascii_lowercase
        for a in alphabet:
            if a not in dic:
                dic[a] = {}
            for b in alphabet:
                if a == b:
                    dic[a][b] = 0
                else:
                    dic[a][b] = float('inf')

        for (a, b, w) in zip(original, changed, cost):
            dic[a][b] = min(dic[a][b], w)
        
        for k in alphabet:
            for a in alphabet:
                for b in alphabet:
                    dic[a][b] = min(dic[a][b], dic[a][k] + dic[k][b])
        ans = 0
        for a, b in zip(source, target):
            if dic[a][b] == float("inf"):
                return -1
            ans += dic[a][b]
        return ans

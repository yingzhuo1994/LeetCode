# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        count = Counter(arr)
        arr.sort()
        MOD = 10**9 + 7
        ans = 0
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    a = arr[j]
                    b = arr[i] // a
                    if b in count:
                        count[arr[i]] += count[a] * count[b]
            count[arr[i]] %= MOD
            ans += count[arr[i]]
            ans %= MOD
        return ans
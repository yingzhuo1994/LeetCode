# 1st solution
# O(n^3) time | O(n) space
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preXOR = [0 for _ in range(n+1)]
        x = 0
        for i, num in enumerate(arr):
            x ^= num
            preXOR[i] = x
        count = 0
        for i in range(n):
            for k in range(i+1, n):
                for j in range(i+1, k+1):
                    a = preXOR[i-1] ^ preXOR[j-1]
                    b = preXOR[j-1] ^ preXOR[k]
                    if a == b:
                        count += 1
        return count

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preXOR = [0 for _ in range(n+1)]
        x = 0
        for i, num in enumerate(arr):
            x ^= num
            preXOR[i] = x
        count = 0
        for j in range(1, n):
            dic = {}
            for i in range(j):
                a = preXOR[j-1] ^ preXOR[i-1]
                dic[a] = dic.get(a, 0) + 1
            for k in range(j, n):
                b = preXOR[k] ^ preXOR[j-1]
                count += dic.get(b, 0)
        return count
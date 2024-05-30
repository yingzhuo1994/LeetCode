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
# 1st solution
# O((m + n) * log(n)) time | O(n) space
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A = aliceSizes
        B = bobSizes
        B.sort()
        target = sum(A) - sum(B)
        for i in range(len(A)):
            idx = bisect.bisect_left(B, A[i] - target // 2)
            if idx < len(B) and 2 *(A[i] - B[idx]) == target:
                return [A[i], B[idx]]


# 2nd solution
# O((m + n) * log(n)) time | O(n) space
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A = aliceSizes
        B = bobSizes
        target = sum(A) - sum(B)
        if len(A) <= len(B):
            B.sort()
            for i in range(len(A)):
                j = bisect.bisect_left(B, A[i] - target // 2)
                if j < len(B) and 2 * (A[i] - B[j]) == target:
                    return [A[i], B[j]]
        else:
            A.sort()
            for j in range(len(B)):
                i = bisect.bisect_left(A, B[j] + target // 2)
                if i < len(A) and 2 * (A[i] - B[j]) == target:
                    return [A[i], B[j]]


# 3rd solution
# O(n) time | O(m) space
# where m = len(aliceSizes), n = len(bobSizes)
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A = aliceSizes
        B = bobSizes
        diff = (sum(A) - sum(B)) // 2
        A = set(A)
        for b in set(B):
            a = b + diff
            if a in A:
                return [a, b]
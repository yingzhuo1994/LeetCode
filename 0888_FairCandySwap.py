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
            if 0 <= idx < len(B) and 2 *(A[i] - B[idx]) == target:
                return [A[i], B[idx]]
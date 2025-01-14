# 1st solution
# O(n) time | O(n) space
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dic = {}
        n = len(A)
        ans = [0 for _ in range(n)]
        i = 0
        curSum = 0
        for a, b in zip(A, B):
            dic[a] = dic.get(a, 0) + 1
            dic[b] = dic.get(b, 0) + 1
            if a != b:
                if dic[a] == 2:
                    curSum += 1
                if dic[b] == 2:
                    curSum += 1
            else:
                curSum += 1
            ans[i] = curSum
            i += 1
        return ans
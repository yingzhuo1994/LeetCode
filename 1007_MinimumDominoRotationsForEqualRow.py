# 1st solution
# O(n) time | O(1) space
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        commonValues = set([1, 2, 3, 4, 5, 6])
        for i in range(len(tops)):
            newSet = set()
            if tops[i] in commonValues:
                newSet.add(tops[i])
            if bottoms[i] in commonValues:
                newSet.add(bottoms[i])
            commonValues = newSet
            if len(commonValues) == 0:
                return -1
        ans = float("inf")
        for num in commonValues:
            countTop = 0
            countBottom = 0
            for i in range(len(tops)):
                if tops[i] != num:
                    countTop += 1
                if bottoms[i] != num:
                    countBottom += 1
            ans = min(ans, countTop, countBottom)
        return ans
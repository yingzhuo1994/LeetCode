# 1st solution
# O(n) time | O(n) space
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        inCount = {}
        outCount = {}
        for a, b in paths:
            inCount[b] = inCount.get(b, 0) + 1
            outCount[a] = outCount.get(a, 0) + 1
        for city in inCount:
            if city not in outCount:
                return city
        return ""

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A, B = map(set, zip(*paths))
        return (B - A).pop()
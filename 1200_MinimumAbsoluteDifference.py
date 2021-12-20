# 1st solution, TLE
# O(n^2) time | O(n^2) space
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        minDiff = float("inf")

        arr.sort()
        for i in range(len(arr)):
            for j in range(i):
                a, b = arr[j], arr[i]
                diff = b - a
                if diff > minDiff:
                    continue
                dic[diff].append([a, b])
                minDiff = min(minDiff, diff)
        return dic[minDiff]
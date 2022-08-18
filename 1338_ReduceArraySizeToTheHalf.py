# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        halfLength = (len(arr) + 1) // 2
        countLst = sorted(count.values(), reverse= True)

        ans = 0
        for i in range(len(countLst)):
            ans += 1
            halfLength -= countLst[i]
            if halfLength <= 0:
                break
        return ans

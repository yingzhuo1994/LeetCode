# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic = {}
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = []
            dic[num].append(i)
        ans = 0
        for num in dic:
            lst = dic[num]
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    val = lst[i] * lst[j]
                    if val % k == 0:
                        ans += 1
        return ans
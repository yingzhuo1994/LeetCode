# 1st solution
# O(n) time | O(k) space
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {i: 0 for i in range(k)}
        for num in arr:
            r = num % k
            dic[r] = dic.get(r, 0) + 1
        if dic[0] & 1:
            return False
        for a in range(1, (k + 1) // 2):
            b = k - a
            if dic[a] != dic[b]:
                return False
        if k % 2 == 0:
            if dic[k // 2] & 1:
                return False
        return True
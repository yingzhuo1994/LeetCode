# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dic = {}
        ans = 1
        for num in arr:
            prev = num - difference
            if prev in dic:
                dic[num] = max(dic.get(num, 0), dic[prev] + 1)
                ans = max(ans, dic[num])
            else:
                dic[num] = 1
        
        return ans
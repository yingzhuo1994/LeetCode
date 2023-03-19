# 1st solution
# O(1) time | O(1) space
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst = [int(d) for d in str(n)]
        k = len(lst)
        i = k - 2
        while i >= 0 and lst[i] >= lst[i + 1]:
            i -= 1
        
        if i < 0:
            return -1
        
        ans = -1
        for j in reversed(range(i + 1, k)):
            if lst[j] > lst[i]:
                # newLst = lst[:i] + [lst[j]] + lst[i+1:j] + lst[j+1:]
                lst[i], lst[j] = lst[j], lst[i]
                lst[i+1:] = sorted(lst[i+1:])
                ans = int("".join([str(d) for d in lst]))
                break
        if ans <= 2**31 -1:
            return ans
        return -1
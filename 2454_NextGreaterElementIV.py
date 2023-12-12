# 1st solution
# O(n) time | O(n) space
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s = []
        t = []
        for i, x in enumerate(nums):
            while t and nums[t[-1]] < x:
                ans[t.pop()] = x  # t 栈顶的下下个更大元素是 x
            j = len(s) - 1
            while j >= 0 and nums[s[j]] < x:
                j -= 1  # s 栈顶的下一个更大元素是 x
            t += s[j + 1:]  # 把从 s 弹出的这一整段元素加到 t
            del s[j + 1:]  # 弹出一整段元素
            s.append(i)  # 当前元素（的下标）加到 s 栈顶
        return ans
# 1st solution
# O(n) time | O(n) space
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack1 = []
        stack2 = []
        for i, x in enumerate(nums):
            while stack2 and nums[stack2[-1]] < x:
                ans[stack2.pop()] = x  # t 栈顶的下下个更大元素是 x
            j = len(stack1) - 1
            while j >= 0 and nums[stack1[j]] < x:
                j -= 1  # s 栈顶的下一个更大元素是 x
            stack2 += stack1[j + 1:]  # 把从 s 弹出的这一整段元素加到 t
            del stack1[j + 1:]  # 弹出一整段元素
            stack1.append(i)  # 当前元素（的下标）加到 s 栈顶
        return ans
# 1st solution
# O(n^T) time | O(T) space
# where T = target
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.ans = 0
        def dfs(idx, lst, value):
            if value == 0:
                count = Counter(lst)
                n = len(lst)
                number = factorial(n)

                for k, v in count.items():
                    number //= factorial(v)
                self.ans += number

                return
            for i in range(idx, len(nums)):
                if value - nums[i] >= 0:
                    dfs(i, lst + [i], value - nums[i])
                else:
                    break
        nums.sort()
        dfs(0, [], target)
        return self.ans

# 2nd solution
# O(n * T) time | O(T) space
# where T = target
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.ans = 0
        nums.sort()
        level = {target: 1}
        while level:
            newLevel = {}
            for value in level:
                if value == 0:
                    self.ans += level[value]
                    continue
    
                for i, num in enumerate(nums):
                    if value < num:
                        break
                    newTarget = value - num
                    newLevel[newTarget] = newLevel.get(newTarget, 0) + level[value]
            
            level = newLevel

        return self.ans
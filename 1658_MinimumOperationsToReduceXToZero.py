# 1st solution
# O(nlog(n)) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        frontSums = nums[:]
        for i in range(1, len(nums)):
            frontSums[i] += frontSums[i-1]

        backSums = nums[:]
        for i in reversed(range(len(nums) - 1)):
            backSums[i] += backSums[i+1]

        ans = float("inf")

        for i in range(n):
            if frontSums[i] == x:
                ans = min(ans, i + 1)
        for i in reversed(range(n)):
            if backSums[i] == x:
                ans = min(ans, n - i)
            j = bisect.bisect_left(frontSums, x - backSums[i])
            if j < i and frontSums[j] + backSums[i] == x:
                ans = min(ans, j + 1 + n - i)
        
        if ans == float("inf"):
            return -1
        else:
            return ans
            
# 2nd solution
# O(n) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        frontSums = nums[:]
        for i in range(1, len(nums)):
            frontSums[i] += frontSums[i-1]

        backSums = nums[:]
        for i in reversed(range(len(nums) - 1)):
            backSums[i] += backSums[i+1]

        dic = {}
        for i, value in enumerate(frontSums):
            dic[value] = i
        ans = float("inf")

        for i in range(n):
            if frontSums[i] == x:
                ans = min(ans, i + 1)
            if frontSums[i] > x:
                break
        for i in reversed(range(n)):
            if backSums[i] == x:
                ans = min(ans, n - i)
            if backSums[i] > x:
                break

        for i in reversed(range(n)):
            leftTarget = x - backSums[i]
            if leftTarget <= 0:
                break
            if leftTarget in dic:
                j = dic[leftTarget]
                if j < i:
                    ans = min(ans, n - i + j + 1)
        
        if ans == float("inf"):
            return -1
        else:
            return ans
            
# 3rd solution
# O(n) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1

# 4th solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        start = 0
        curSum = 0
        ans = -1
        for end in range(len(nums)):
            curSum += nums[end]
            while curSum >= target:
                if curSum == target:
                    ans = max(ans, end - start + 1)
                curSum -= nums[start]
                start += 1
        return -1 if ans == -1 else len(nums) - ans
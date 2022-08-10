# 1st solution
# O(n^3) time | O(n^2) space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        dic = defaultdict(list)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                curSum = nums[i] + nums[j]
                newTarget = target - curSum
                if newTarget in dic:
                    for lst in dic[newTarget]:
                        newLst = lst + [nums[i], nums[j]]
                        if ans and ans[-1] == newLst:
                            continue
                        ans.append(newLst)
            
            for k in range(i):
                if k != 0 and nums[k] == nums[k - 1]:
                    continue
                curSum = nums[k] + nums[i]
                newLst = [nums[k], nums[i]]
                if curSum in dic and dic[curSum][-1] == newLst:
                    continue
                dic[curSum].append(newLst)
        if len(ans) <= 1:
            return ans
        array = sorted([sorted(lst) for lst in ans])
        ans = [array[0]]
        for i in range(len(array) - 1):
            if array[i + 1] != array[i]:
                ans.append(array[i + 1])
        return ans

# 2nd solution
# O(n^3) time | O(n^2) space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def KSum(l, r, target, k, result, results):
            if r-l+1 < k or k < 2 or target < nums[l]*k or target > nums[r]*k:  # early termination
                return
            if k == 2: # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(l, r+1):
                    if i == l or nums[i-1] != nums[i]:
                        KSum(i+1, r, target-nums[i], k-1, result+[nums[i]], results)

        nums.sort()
        results = []
        KSum(0, len(nums)-1, target, 4, [], results)
        return results
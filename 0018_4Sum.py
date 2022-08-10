# 1st solution
# O(n^2) time | O(n^2) space
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
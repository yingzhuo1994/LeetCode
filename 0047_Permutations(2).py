# 1st solution
# O(n * n!) time | O(n * n!) space
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        while True:
            ans.append(nums[:])
            self.getNextPermutation(nums)
            if ans[0] == nums:
                break
        return ans
    
    def getNextPermutation(self, nums):
        lastDecIdx = len(nums) - 1
        while lastDecIdx > 0 and nums[lastDecIdx] <= nums[lastDecIdx - 1]:
            lastDecIdx -= 1
        
        if lastDecIdx == 0:
            self.reverse(nums, 0)
        else:
            prevIdx = lastDecIdx - 1
            self.reverse(nums, lastDecIdx)
            nextIdx = self.getNextLargerIdx(nums, lastDecIdx, nums[prevIdx])
            self.swap(nums, prevIdx, nextIdx)
    
    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    

    def getNextLargerIdx(self, nums, start, value):
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] <= value:
                start = mid + 1
            else:
                end = mid - 1
        return start

# 2nd solution, backtrack
# O(n * n!) time | O(n * n!) space
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
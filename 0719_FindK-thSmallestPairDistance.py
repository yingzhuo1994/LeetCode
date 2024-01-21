# 1st solution, MLE
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        array = [abs(nums[i] - nums[j]) for i in range(n) for j in range(i)]
        array.sort()
        return array[k - 1]

# 2nd solution
# O(n * log(D)) time | O(n) space
# D is the largest distance among all dist pairs
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        minDist, maxDist = 0, nums[-1] - nums[0]
        while minDist < maxDist:
            targetDist = minDist + (maxDist - minDist) // 2
            start = 0
            count = 0
            i = 1
            while i < n:
                dist = nums[i] - nums[start]
                if dist <= targetDist:
                    count += i - start
                    i += 1
                else:
                    start += 1
                if count > k:
                    break
            
            if count >= k:
                maxDist = targetDist
            else:
                minDist = targetDist + 1
        
        return maxDist
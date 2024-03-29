# 1st solution
# O(n) time | O(n) space
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        target = max(counts.keys())
        freq = counts[target]
        if freq < k:
            return 0
        def countHelper(start, end, diff):
            ans = 0
            count = 0
            j = start
            for i in range(start, end, diff):
                if nums[i] == target:
                    count += 1
                while count >= k:
                    if nums[j] == target:
                        count -= 1
                    j += diff
                    if count == k - 1:
                        count += 1
                        j -= diff
                        break
                                
                if count >= k:
                    ans += abs(j - start + 1)
            return ans
        return countHelper(0, len(nums), 1)
        
# 2nd solution
# O(n) time | O(1) space
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        start = 0
        count = 0
        res = 0
        for i in range(len(nums)):
            count += nums[i] == target
            while count >= k:
                count -= nums[start] == target
                start += 1
            res += start
        return res
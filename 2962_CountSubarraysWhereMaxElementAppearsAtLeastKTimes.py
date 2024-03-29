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
        

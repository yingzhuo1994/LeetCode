# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curSum = [0]
        for num in nums:
            curSum.append(curSum[-1] + num)
        
        ans = 0
        def binarySearch(idx):
            start = 0
            end = idx
            while start < end:
                mid = start + (end - start) // 2
                val = curSum[idx] - curSum[mid]
                if val * (idx - mid) < k:
                    end = mid
                else:
                    start = mid + 1
            return idx - start
        
        for i in range(1, len(curSum)):
            ans += binarySearch(i)
        
        return ans
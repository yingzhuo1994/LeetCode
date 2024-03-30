# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        dic = {}
        last = {}
        minHeap = []
        distinct = 0
        ans = 0
        start = 0
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
            last[num] = i
            heappush(minHeap, [i, num])
            if dic[num] == 1:
                distinct += 1
            while distinct > k:
                dic[nums[start]] -= 1
                if dic[nums[start]] == 0:
                    distinct -= 1
                start += 1
            while minHeap and (minHeap[0][0] < last[minHeap[0][1]] or dic[minHeap[0][1]] == 0):
                heappop(minHeap)
            if distinct == k:
                ans += minHeap[0][0] - start + 1

        return ans 
            
            

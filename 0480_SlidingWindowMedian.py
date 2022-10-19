# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap = []
        minHeap = []
        ans = []
        # create the initial left and right heap
        for i, num in enumerate(nums[:k]): 
            heappush(maxHeap, (-num, i))
        
        for i in range(k-k//2):
            num, idx = heappop(maxHeap)
            heappush(minHeap, (-num, idx))
            
        ans.append(minHeap[0][0]/1. if k%2 else (minHeap[0][0] - maxHeap[0][0])/2.)
        for i in range(k, len(nums)):
            num = nums[i]
            if num >= minHeap[0][0]:
                heappush(minHeap,(num, i))        # minHeap +1
                if nums[i - k] <= minHeap[0][0]:     # maxHeap-1, unbalanced
                    heappush(maxHeap, (-minHeap[0][0], minHeap[0][1]))
                    heappop(minHeap)
                # else: pass                # minHeap-1, balanced
            else:
                heappush(maxHeap,(-num, i))        # maxHeap +1
                if nums[i - k] >= minHeap[0][0]:     # minHeap-1, unbalanced
                    heappush(minHeap, (-maxHeap[0][0], maxHeap[0][1]))
                    heappop(maxHeap)
                # else: pass                # maxHeap-1, balanced
            while(maxHeap and maxHeap[0][1] <= i - k): heappop(maxHeap)  # lazy-deletion
            while(minHeap and minHeap[0][1] <= i - k): heappop(minHeap)  # lazy-deletion
            if k & 1:
                ans.append(minHeap[0][0]/1.)
            else:
                ans.append((minHeap[0][0] - maxHeap[0][0])/2.)
                
        return ans
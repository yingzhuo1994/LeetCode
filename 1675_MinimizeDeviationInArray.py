# 1st solution
# O(m*log(n)) time | O(n) space
# where n is the length of nums and m is total number of candidates,
# we can estimate m = O(n*log(K)), where K is the biggest number.
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            tmp = num
            while tmp%2 == 0: tmp//=2
            heap.append((tmp, max(num, tmp*2)))
        
        Max = max(i for i,j in heap)
        heapify(heap)
        ans = float("inf")

        while True:
            num, limit = heappop(heap)
            ans = min(ans, Max - num)
            if num < limit:
                heappush(heap, (num*2, limit))
                Max = max(Max, num*2)
            else:
                break
        return ans

# 2nd solution
# O(m*log(n)) time | O(n) space
# where n is the length of nums and m is total number of candidates,
# we can estimate m = O(n*log(K)), where K is the biggest number.
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        stack = []
        low = float("inf")
        for num in nums:
            if num & 1:
                num *= 2
            heappush(stack, -num)
            low = min(low, num)
        ans = -stack[0] - low
        while (-stack[0]) % 2 == 0:
            num = -heappop(stack)
            num //= 2
            low = min(low, num)
            heappush(stack, -num)
            ans = min(ans, -stack[0] - low)
        
        return ans
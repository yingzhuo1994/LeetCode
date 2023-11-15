# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i-1] + 1, arr[i])
        return arr[-1]

# 2nd solution
# O(n) time | O(n) space 
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        count = [0 for _ in range(n + 1)]
        for i in range(n):
            arr[i] = min(arr[i], n)
            count[arr[i]] += 1

        for j in reversed(range(1, n)):
            count[j] += count[j + 1]

        ans = n

        for i in range(1, n):
            if i >= ans:
                break
            ans = min(ans, i + count[i + 1])
        
        return ans
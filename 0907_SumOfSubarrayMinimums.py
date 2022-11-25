# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        ans = sum(arr)
        level = arr
        for L in range(1, n):
            newLevel = []
            for i in range(n - L):
                value = min(level[i], arr[i+L])
                ans += value
                newLevel.append(value)
            ans %= MOD
            level = newLevel
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = [-1]
        arr.append(-1)
        sum_of_minimums = 0;

        for i in range(len(arr) ):
            while arr[i] < arr[stack[-1]]:
                mid = stack.pop()
                left_boundary = stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                count = (mid - left_boundary) * (right_boundary - mid)
                sum_of_minimums += (count * arr[mid])

            stack.append(i)
        
        return sum_of_minimums % MOD
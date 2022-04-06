# 1st solution
# O(n^2) time | O(log(n)) space 
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        arr.sort()

        for i, first in enumerate(arr):
            newTarget = target - first
            j, k = i + 1, len(arr) - 1
            while j < k:
                if arr[j] + arr[k] < newTarget:
                    j += 1
                elif arr[j] + arr[k] > newTarget:
                    k -= 1
                elif arr[j] != arr[k]: # We have arr[j] + arr[k] == newTarget
                    # Let's count "left": the number of arr[j] == arr[j+1] == arr[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) // 2 pairs.
                    ans += (k-j+1) * (k-j) // 2
                    ans %= MOD
                    break

        return ans

# 2nd solution
# O(n + w^2) time | O(w) space
# where n is the length of arr, and w is the maximum possible value of arr[i] 
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        w = 101
        count = [0] * w
        for num in arr:
            count[num] += 1

        ans = 0

        # All different
        for x in range(w):
            for y in range(x + 1, w):
                z = target - x - y
                if y < z < w:
                    ans += count[x] * count[y] * count[z]
                    ans %= MOD

        # two numbers are the same
        for x in range(w):
            z = target - 2 * x
            if z != x and 0 <= z < w:
                ans += count[x] * (count[x] - 1) // 2 * count[z]
                ans %= MOD

        # three numbers are the same
        if target % 3 == 0:
            x = target // 3
            if 0 <= x < w:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                ans %= MOD

        return ans
# 1st solution
# O(n) time | O(1) space
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        maxStr = ""
        for i in range(len(num) - 2):
            if num[i:i+3] == num[i] * 3 and int(num[i:i+3]) > ans:
                ans = int(num[i:i+3])
                maxStr = num[i:i+3]
        return maxStr
# 1st solution
# O(n) time | O(n) space
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx = 0
        ans = []
        for i in range(1, n + 1):
            ans.append("Push")
            if target[idx] == i:
                idx += 1
            else:
                ans.append("Pop")
            if idx == len(target):
                break
        return ans
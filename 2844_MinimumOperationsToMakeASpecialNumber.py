# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumOperations(self, num: str) -> int:
        def deleteNum(target):
            j = len(target) - 1
            for i in reversed(range(len(num))):
                if num[i] == target[j]:
                    j -= 1
                if j < 0:
                    return len(num) - i - 2
            return len(num)
        
        ans = min([deleteNum(t) for t in ["00", "25", "50", "75"]])
        cnt = Counter(num)
        if cnt["0"] == 1:
            ans = min(ans, len(num) - 1)
        return ans
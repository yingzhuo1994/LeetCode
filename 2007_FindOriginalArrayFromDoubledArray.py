# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            return []
        
        count = collections.Counter(changed)
        nums = sorted(list(count.keys()))
        original = []
        for num in nums:
            if count[num] > 0:
                if count[num*2] >= count[num]:
                    if num != 0:
                        original.extend([num] * count[num])
                    else:
                        original.extend([num] * (count[num] // 2))
                    count[num*2] -= count[num]
                else:
                    return []
        return original

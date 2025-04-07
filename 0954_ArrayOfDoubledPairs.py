# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        pos = [num for num in arr if num >= 0]
        neg = [num for num in arr if num < 0]
        pos.sort()
        neg.sort(reverse=True)
        
        cnt1 = Counter(pos)
        cnt2 = Counter(neg)

        for num in pos:
            if cnt1[num] == 0:
                continue
            if num == 0:
                if cnt1[num] & 1:
                    return False
                cnt1[num] = 0
                continue

            val = 2 * num
            if cnt1[val] < cnt1[num]:
                return False
            cnt1[val] -= cnt1[num]
            cnt1[num] = 0
        
        for num in neg:
            if cnt2[num] == 0:
                continue
            val = 2 * num
            if cnt2[val] < cnt2[num]:
                return False
            cnt2[val] -= cnt2[num]
            cnt2[num] = 0
        
        return True
            

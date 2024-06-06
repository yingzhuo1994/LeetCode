# 1st solution
# O(n * log(n) + kn) time | O(n) space
# where n = len(hand), k = groupSize
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        cnt = Counter(hand)
        keys = sorted(cnt.keys())
        idx = 0
        while idx < len(keys):
            if cnt[keys[idx]] > 0:
                val = cnt[keys[idx]]
                cnt[keys[idx]] = 0
                for i in range(idx + 1, idx + groupSize):
                    if i >= len(keys) or cnt[keys[i]] < val or keys[i] - keys[i-1] != 1:
                        return False
                    cnt[keys[i]] -= val
            idx += 1
        return all([cnt[keys[i]] == 0 for i in range(idx, len(keys))] + [True]) 



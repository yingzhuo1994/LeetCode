# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        curVal = sum(cards[:cnt])
        if not (curVal & 1):
            return curVal
        ans = 0
        i = cnt - 1
        while i >= 0:
            if cards[i] & 1:
                break
            i -= 1
        if i >= 0:
            for j in range(cnt, len(cards)):
                if not (cards[j] & 1):
                    ans = max(ans, curVal - cards[i] + cards[j])
                    break
        
        i = cnt - 1
        while i >= 0:
            if not (cards[i] & 1):
                break
            i -= 1

        if i >= 0:
            for j in range(cnt, len(cards)):
                if cards[j] & 1:
                    ans = max(ans, curVal - cards[i] + cards[j])
                    break
        return ans

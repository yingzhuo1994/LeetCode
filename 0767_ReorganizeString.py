# 1st solution
# O(n) time | O(n) space
class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)
        f = max(count.values())
        if n & 1:
            if f > (n + 1) // 2:
                return ""
        else:
            if f > n // 2:
                return ""
        
        pairs = [[freq, ch] for ch, freq in count.items()]
        pairs.sort()
        pairs.reverse()

        ans = ["" for _ in range(n)]
        idx = 0
        for freq, ch in pairs:
            for _ in range(freq):
                ans[idx] = ch
                idx += 2
                if idx >= n:
                    idx = 1
        
        return "".join(ans)

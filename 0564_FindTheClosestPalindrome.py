class Solution:
    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [str(10**k + d) for k in (m-1, m) for d in (-1, 1)]
        prefix = n[:(m+1)//2]
        p = int(prefix)
        for start in map(str, (p-1, p, p+1)):
            candidates.append(start + (start[:-1] if m & 1 else start)[::-1])
        
        def delta(x):
            return abs(int(n) - int(x))
        
        ans = None
        for cand in candidates:
            if cand != n and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans
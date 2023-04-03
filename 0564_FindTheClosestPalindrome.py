class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        candidates = [str(10**k + d) for k in (k-1, k) for d in (-1, 1)]
        prefix = n[:(k+1)//2]
        p = int(prefix)
        for start in map(str, (p-1, p, p+1)):
            candidates.append(start + (start[:-1] if k%2 else start)[::-1])
        
        def delta(x):
            return abs(int(n) - int(x))
        
        ans = None
        for cand in candidates:
            if cand != n and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans
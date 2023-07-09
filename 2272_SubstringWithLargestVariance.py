# 1st solution, TLE
# O(n^2) time | O(1) space
class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        ans = 0
        for length in range(1, n + 1):
            dic = {}
            start = 0
            for i in range(n):
                ch = s[i]
                dic[ch] = dic.get(ch, 0) + 1
                if i - start + 1 > length:
                    dic[s[start]] -= 1
                    if dic[s[start]] == 0:
                        dic.pop(s[start])
                    start += 1
                diff = max(dic.values()) - min(dic.values())
                ans = max(ans, diff)
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def largestVariance(self, s: str) -> int:
        def solveOne(a, b, s):
            max_var = 0
            
            var = 0
            has_b = False
            first_b = False # first element of the currently considered subarray is b
            
            for c in s:
                if c == a:
                    var += 1
                
                elif c == b:
                    has_b = True
                    
                    if first_b and var >= 0: # "shift right" and save a 1 in the current sum to be able to properly maximise it
                        # we can only do this when we know that we have a `b` at the start of our current subarray, and we'll only ever have a single b at the start
                        # always followed by an a, due to the next rule
                        first_b = False 
                    elif (var - 1) < 0: # restart the subarray from this b (inclusive) onwards
                        # this rule ensures we skip double-b's, every subarray will always end up being `ba....`, `[bb]a` would become `b[b]a` -> `b[ba]`
                        first_b = True 
                        var = -1
                    else:
                        var -= 1 # var will always be >= 0 in this case
                
                if has_b and var > max_var:
                    max_var = var
            
            return max_var
        count = Counter(s)
        letters = list(count.keys())
        ans = 0
        for minCh in letters:
            for maxCh in letters:
                if minCh == maxCh:
                    continue
                ans = max(ans, solveOne(minCh, maxCh, s))
        return ans
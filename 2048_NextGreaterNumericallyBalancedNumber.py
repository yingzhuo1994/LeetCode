# 1st solution
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0:
            return 1
        s = str(n)
        d = len(s)
        if d == 1:
            return 22
        def seperate(k, start):
            if k == 0:
                return [""]
            ans = []
            for i in range(start, k + 1):
                for t in seperate(k - i, i + 1):
                    ans.append(str(i) + t)
            return ans
        
        def find(t):
            dic = {int(ch): int(ch) for ch in t}
            keys = sorted(dic.keys())
            total = sum(keys)
            candidates = []
            def dfs(idx, dic, lst):
                if idx == total:
                    num = int("".join(lst))
                    if num > n:
                        candidates.append(num)
                    return
 
                for key in keys:
                    if dic[key] > 0:
                        dic[key] -= 1
                        dfs(idx + 1, dic, lst + [str(key)])
                        dic[key] += 1

            dfs(0, dic, [])
            return min(candidates) if candidates else -1
        
        candidates = seperate(d, 1) + seperate(d + 1, 1)
        ans = float("inf")
        for candidate in candidates:
            v = find(candidate)
            if v == -1:
                continue
            ans = min(ans, v)
        
        return ans



# 1st solution
# O(n^3) time | O(n^3) space
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def helper(t):
            if len(t) == 1 and t[0] == "0":
                return [t]
            val = int(t)
            if str(val) != t:
                if val == 0 or t[-1] == "0":
                    return []
                return [t[0] + "." + t[1:]]
            lst = [t]
            if t[-1] != "0":
                for i in range(len(t) - 1):
                    lst.append(t[:i + 1] + "." + t[i+1:])
            return lst
        
        ans = []
        s = s[1:-1]
        n = len(s)
        for i in range(1, n):
            front = helper(s[:i])
            if len(front) == 0:
                continue
            back = helper(s[i:])
            if len(back) == 0:
                continue
            ans.extend([a + ", " + b for a in front for b in back])
        return [f"({t})" for t in ans]
# 1st solution
# O(n * (log(k))^2) time | O(n) space
# where n = len(num), k = 2^31
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        def dfs(idx, lst):
            if idx == n:
                if len(lst) < 3:
                    return []
                return lst
            if len(lst) >= 2:
                target = lst[-1] + lst[-2]
                if target > 2**31:
                    return []
                if num[idx] == "0":
                    if all(ch == "0" for ch in num):
                        return [0 for _ in range(n)]
                    return []
                else:
                    d = min(len(str(lst[-1])), len(str(lst[-2])))
                    for j in range(idx + d, n + 1):
                        val = int(num[idx:j])
                        if val == target:
                            lst.append(val)
                            ans = dfs(j, lst)
                            if len(ans) > 0:
                                return ans
                            lst.pop()
                            return []
                        elif val > target:
                            return []
            else:
                for j in range(idx + 1, n + 1):
                    val = int(num[idx:j])
                    lst.append(val)
                    ans = dfs(j, lst)
                    if len(ans) > 0:
                        return ans
                    lst.pop()
                    if val == 0:
                        return []
            return []
        
        return dfs(0, [])
# 1st solution, MLE
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        totalDist = sum(dist)
        goalDist = speed * hoursBefore
        if totalDist > goalDist:
            return -1
        
        memo = {}
        def dfs(idx, prevDist, sumDist):
            key = (idx, prevDist, sumDist)
            if key in memo:
                return memo[key]
            if sumDist > goalDist:
                return -1
            d = dist[idx]
            curDist = prevDist + d
            if idx == len(dist) - 1:
                if curDist + sumDist <= goalDist:
                    memo[key] = 0
                    return 0
                else:
                    memo[key] = -1
                    return -1
            q, r = divmod(curDist, speed)
            if r == 0:
                memo[key] = dfs(idx + 1, 0, sumDist + curDist)
            else:
                rest = dfs(idx + 1, 0, sumDist + ((q + 1) * speed))
                notRest = dfs(idx + 1, curDist, sumDist)
                if rest == -1 and notRest == -1:
                    memo[key] = -1
                elif rest == -1:
                    memo[key] = notRest + 1
                elif notRest == -1:
                    memo[key] = rest
                else:
                    memo[key] = min(rest, notRest + 1)
            return memo[key]
        
        ans = dfs(0, 0, 0)
        return ans

# 2nd solution
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1
        f = [0] * len(dist)
        for i in count(0):
            pre = 0
            for j, d in enumerate(dist[:-1]):
                tmp = f[j + 1]
                f[j + 1] = (f[j] + d + speed - 1) // speed * speed
                if i:
                    f[j + 1] = min(f[j + 1], pre + d)
                pre = tmp
            if f[-1] + dist[-1] <= speed * hoursBefore:
                return i


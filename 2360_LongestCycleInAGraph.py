# 1st solution, TLE
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cycleSet = set()
        n = len(edges)
        ans = -1
        for i in range(n):
            if i in cycleSet:
                continue
            slow = i
            fast = i
            # print(i)
            foundCycle = False
            while fast >= 0 and edges[fast] >= 0:
                slow = edges[slow]
                fast = edges[fast]
                fast = edges[fast]
                # print(slow, fast)
                if slow == fast:
                    foundCycle = True
                    break
            if foundCycle:
                # print("find cycle")
                count = 0
                while slow not in cycleSet:
                    count += 1
                    cycleSet.add(slow)
                    slow = edges[slow]
                ans = max(ans, count)
        return ans

# 1st solution, TLE
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = collections.defaultdict(list)
        for i, num in enumerate(arr):
            dic[num].append(i)
        
        visited = set([0])
        level = set([0])
        step = 0
        while len(visited) < len(arr):
            newLevel = set()
            for k in level:
                if k == len(arr) - 1:
                    return step
                if k - 1 >= 0 and k - 1 not in visited:
                    newLevel.add(k - 1)
                if k + 1 < len(arr) and k + 1 not in visited:
                    newLevel.add(k + 1)
                for idx in dic[arr[k]]:
                    if idx not in visited:
                        newLevel.add(idx)
            level = newLevel
            visited = visited.union(level)
            step += 1
        return step
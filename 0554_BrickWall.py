# 1st solution
# O(mn) time | O(m) space
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        for line in wall:
            w = 0
            for brick in line[:-1]:
                w += brick
                dic[w] += 1

        return len(wall) - max(list(dic.values()) + [0])
# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        monsters = [dist[i] / speed[i] for i in range(n)]
        monsters.sort()

        count = 0
        for i, t in enumerate(monsters):
            if t <= i:
                return count
            else:
                count += 1
        return count

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        count = [0 for _ in range(n)]

        for i in range(n):
            # 怪物需要在time时间内被消灭
            time = (dist[i] - 1) // speed[i]

            # time >= n的怪物不用管
            if time < n:
                count[time] += 1
        
        # 能够击杀怪物的数量
        kill = 0
        for i in range(n):
            # 每过一秒能多击杀一只怪物
            kill += 1  

            # 减去限定时间需要击杀的怪物
            kill -= count[i]
            
            # 如果怪物到达城市
            if kill < 0:
                return i + 1

        return n
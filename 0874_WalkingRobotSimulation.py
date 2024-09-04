# 1st solution
# O(n + m) time | O(m) space
# where n = len(commands) and m = len(obstacles)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        pos_x, pos_y = 0, 0
        dir_x, dir_y = 0, 1
        ans = 0
        calc_dist = lambda x, y: x**2 + y**2
        for command in commands:
            if command == -1:
                dir_x, dir_y = dir_y, -dir_x
            elif command == -2:
                dir_x, dir_y = -dir_y, dir_x
            else:
                for _ in range(command):
                    x = pos_x + dir_x
                    y = pos_y + dir_y
                    print(x, y, (dir_x, dir_y))
                    if (x, y) in obstacles:
                        break
                    pos_x = x
                    pos_y = y
                    ans = max(ans, calc_dist(pos_x, pos_y))
        return ans
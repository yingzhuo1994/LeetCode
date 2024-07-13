# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ans = []
        stack = []
        n = len(positions)
        robots = [[p, d, h, i] for i, p, d, h in zip(list(range(n)), positions, directions, healths)]
        robots.sort()
        for p, d, h, i in robots:
            alive = True
            if d == "L":
                while stack:
                    h1, i1 = stack.pop()
                    if h1 > h:
                        alive = False
                        h1 -= 1
                        stack.append([h1, i1])
                        break
                    elif h1 == h:
                        alive = False
                        break
                    else:
                        alive = True
                        h -= 1
                if alive:
                    ans.append([h, i])
            else:
                stack.append([h, i])
        ans.extend(stack)
        ans.sort(key=lambda v: v[1])
        return [h for h, _ in ans]


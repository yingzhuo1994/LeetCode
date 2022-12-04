# 1st solution
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        n = len(stones)
        if n == 2:
            return True
        dic = {num: i for i, num in enumerate(stones)}
        level = deque([[1, 1]])
        visited = set([(1, 1)])
        while level:
            idx, k = level.popleft()
            for step in [k - 1, k, k + 1]:
                if step == 0:
                    continue
                place = idx + step
                if place == stones[-1]:
                    return True
                if place not in dic or (place, step) in visited:
                    continue
                visited.add((place, step))
                level.append([place, step])
        return False

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        n = len(stones)
        if n == 2:
            return True
        dp = [[False for _ in range(n + 1)] for _ in range(n)]
        dp[0][1] = True
        
        for i in range(n):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff < 0 or diff > i or not dp[j][diff]:
                    continue
                dp[i][diff] = True
                if diff - 1 >= 0:
                    dp[i][diff - 1] = True
                if diff + 1 <= n:
                    dp[i][diff + 1] = True
                if i == n - 1:
                    return True

        return False

# 3rd solution
# O(n^2) time | O(n^2) space
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        n = len(stones)
        if n == 2:
            return True
        dp = [set() for _ in range(n)]
        dp[0].add(1)
        
        for i in range(1, n):
            # check all the previous stones from where the jumps are possible
            for j in range(i):
                # store the move value required from jth to ith stone
                diff = stones[i] - stones[j]
                # check if that move value is present in jth stone
                if diff in dp[j]:
                    # If possible, then add possibilities of move values in the ith stone set
                    dp[i].add(diff - 1)
                    dp[i].add(diff)
                    dp[i].add(diff + 1)
                    if i == n - 1:
                        return True

        return False
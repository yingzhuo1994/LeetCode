# 1st solution
# O(n) time | O(n) space
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        q = deque([[i, 0] for i in range(n)])
        if k > 2 * n:
            k = (k - n) % n + n
        while True:
            first = q.popleft()
            second = q.popleft()
            if skills[first[0]] > skills[second[0]]:
                winner = first
                loser = second
            else:
                winner = second
                loser = first
            winner[1] += 1
            loser[1] = 0
            if winner[1] >= k:
                return winner[0]
            q.appendleft(winner)
            q.append(loser)
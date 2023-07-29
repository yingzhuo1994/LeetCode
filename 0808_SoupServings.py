# 1st solution, TLE
class Solution:
    def soupServings(self, n: int) -> float:
        plans = [[100, 0], [75, 25], [50, 50], [25, 75]]

        ans = 0

        state = {(n, n): 1.0}
        while state:
            newState = {}
            for key, p in state.items():
                A, B = key
                for a, b in plans:
                    leftA = A - a
                    leftB = B - b
                    if leftA <= 0:
                        if leftA < leftB:
                            ans += p * 0.25
                        elif leftA == leftB:
                            ans += 0.5 * p * 0.25
                    if leftA > 0 and leftB > 0:
                        newState[(leftA, leftB)] = newState.get((leftA, leftB), 0) + p * 0.25

            state = newState
        
        return ans
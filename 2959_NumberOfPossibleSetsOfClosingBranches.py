# 1st solution
# O(2^n * n^3) time | O(n^3) space
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        matrix = [[float(inf) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
        for a, b, w in roads:
            if w > maxDistance:
                continue
            matrix[a][b] = min(matrix[a][b], w)
            matrix[b][a] = matrix[a][b]
        ans = 0
        for mask in range(1 << n):
            cities = [i for i in range(n) if mask & (1 << i)]
            if len(cities) <= 1:
                ans += 1
            else:
                smallMap = {a: {b: matrix[a][b] for b in cities} for a in cities}
                for c in cities:
                    for a in cities:
                        for b in cities:
                            smallMap[a][b] = min(smallMap[a][b], smallMap[a][c] + smallMap[c][b])
                invalid = False
                for a in cities:
                    for b in cities:
                        if smallMap[a][b] > maxDistance:
                            invalid = True
                            break
                    if invalid:
                        break

                if not invalid:
                    ans += 1

        return ans

# 1st solution
# O(sqrt(m)) time | O(n) space
# where m = candies, n = num_people
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        ans = [0] * n
        val = 1
        while candies > 0:
            idx = (val - 1) % n
            ans[idx] += min(val, candies)
            candies -= val
            val += 1
        return ans


# 2nd solution
# O(n) time | O(n) space
# where m = candies, n = num_people
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        a = n * n
        b = 2 * n * n + n
        c = n * n + n - 2 * candies
        k = (sqrt(b**2 - 4 * a * c) - b) / (2 * a)
        k = floor(k)

        ans = [(i + k * n + i) * (k + 1) // 2 for i in range(1, n + 1)]

        candies -= ((k + 1) * n**2 + n) * (k + 1) // 2

        i = 0
        val = (k+1) * n
        while candies > 0:
            val += 1
            ans[i] += min(candies, val)
            candies -= val
            i += 1

        return ans

# 3rd solution
# O(n) time | O(n) space
# where m = candies, n = num_people
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        x = int(math.sqrt(candies * 2 + 0.25) - 0.5)
        res = [0] * n
        for i in range(n):
            m = x // n + (x % n > i)
            res[i] = m * (i + 1) + m * (m - 1) // 2 * n
        res[x % n] += candies - x * (x + 1) // 2
        return res
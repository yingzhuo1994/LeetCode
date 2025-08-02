# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i, val in enumerate(rating):
            left = [rating[j] for j in range(i) if rating[j] < val]
            right = [rating[j] for j in range(i + 1, len(rating)) if rating[j] > val]
            ans += len(left) * len(right)

            left = [rating[j] for j in range(i) if rating[j] > val]
            right = [rating[j] for j in range(i + 1, len(rating)) if rating[j] < val]
            ans += len(left) * len(right)
        return ans


# 2nd solution
# O(n^2) time | O(1) space
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        n = len(rating)
        for i in range(1, n - 1):
            val = rating[i]
            left_low = 0
            left_high = 0
            for j in range(i):
                if rating[j] < val:
                    left_low += 1
                elif rating[j] > val:
                    left_high += 1

            right_low = 0
            right_high = 0
            for j in range(i + 1, n):
                if rating[j] < val:
                    right_low += 1
                elif rating[j] > val:
                    right_high += 1
            ans += left_low * right_high + left_high * right_low

        return ans


# 3rd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        self.maxN = n + 2
        self.c = [0 for _ in range(self.maxN)]
        self.disc = rating[:]
        self.disc.append(-1)
        self.disc.sort()
        iLess = [0 for _ in range(n)]
        iMore = [0 for _ in range(n)]
        kLess = [0 for _ in range(n)]
        kMore = [0 for _ in range(n)]

        for i in range(n):
            id = self.getId(rating[i])
            iLess[i] = self.get(id)
            iMore[i] = self.get(n + 1) - self.get(id)
            self.add(id, 1)
        

        self.c = [0 for _ in range(self.maxN)]
        for i in reversed(range(n)):
            id = self.getId(rating[i])
            kLess[i] = self.get(id)
            kMore[i] = self.get(n + 1) - self.get(id)
            self.add(id, 1)
        
        ans = 0
        for i in range(n):
            ans += iLess[i] * kMore[i] + iMore[i] * kLess[i]
        

        return ans
    
    def getId(self, target):
        low = 0
        high = len(self.disc) - 1
        while low < high:
            mid = (high - low) // 2 + low
            if self.disc[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low
    

    def get(self, p):
        r = 0
        while p > 0:
            r += self.c[p]
            p -= self.lowbit(p)
        return r

    def add(self, p, v):
        while p < self.maxN:
            self.c[p] += v
            p += self.lowbit(p)

    def lowbit(self, x):
        return x & (-x)

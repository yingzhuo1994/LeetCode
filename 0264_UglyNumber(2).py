class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        index = [0, 0, 0]
        vals = [1, 1, 1]
        ans = [1]
        last = 1
        k = 3
        while len(ans) < n:
            for i in range(k):
                if vals[i] == last:
                    vals[i] = ans[index[i]] * primes[i]
                    index[i] += 1
            last = min(vals)
            ans.append(last)
        return last

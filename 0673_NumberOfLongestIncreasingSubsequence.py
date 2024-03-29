# 1st solution
# O(n^2) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        
        dic = {}
        for length, count in dp:
            dic[length] = dic.get(length, 0) + count
        
        maxLnegth = max(dic.keys())
        return dic[maxLnegth]

# 2nd solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        decks, ends_decks, paths = [], [], []
        for num in nums:
            deck_idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if deck_idx > 0:
                l = bisect.bisect(decks[deck_idx-1], -num)
                n_paths = paths[deck_idx-1][-1] - paths[deck_idx-1][l]
                
            if deck_idx == len(decks):
                decks.append([-num])
                ends_decks.append(num)
                paths.append([0, n_paths])
            else:
                decks[deck_idx].append(-num)
                ends_decks[deck_idx] = num
                paths[deck_idx].append(n_paths + paths[deck_idx][-1])
              
        return paths[-1][-1]

# 3rd solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        d, cnt = [], []
        for v in nums:
            i = bisect(len(d), lambda i: d[i][-1] >= v)
            c = 1
            if i > 0:
                k = bisect(len(d[i - 1]), lambda k: d[i - 1][k] < v)
                c = cnt[i - 1][-1] - cnt[i - 1][k]
            if i == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[i].append(v)
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]

    def bisect(n: int, f: Callable[[int], bool]) -> int:
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if f(mid):
                r = mid
            else:
                l = mid + 1
        return l

# 4th solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Discretization and using Fenwick tree
        numsort = sorted(nums)
        nodes = [Node() for _ in range(len(nums) + 1)]
        res = Node()

        for num in nums:
            # Discretization: finding the rank of the current number - 1
            rk = bisect.bisect_left(numsort, num)

            # Finding the length and count of the longest increasing subsequence
            cur = self.query(nodes, rk)
            cur.m += 1
            cur.c = max(cur.c, 1)

            # Updating the global longest increasing subsequence
            res += cur

            # Updating the Fenwick tree
            self.add(nodes, rk + 1, cur, len(nums))

        return res.c

    def add(self, nodes, rk, val, N):
        while rk <= N:
            nodes[rk] += val
            rk += rk & -rk

    def query(self, nodes, rk):
        res = Node()
        while rk:
            res += nodes[rk]
            rk -= rk & -rk
        return res

class Node:
    def __init__(self):
        # max value
        self.m = 0
        # count
        self.c = 0

    def __iadd__(self, b):
        if b.m > self.m:
            self.m = b.m
            self.c = b.c
        elif b.m == self.m:
            self.c += b.c
        return self


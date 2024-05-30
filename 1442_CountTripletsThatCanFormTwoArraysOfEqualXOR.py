# 1st solution
# O(n^3) time | O(n) space
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preXOR = [0 for _ in range(n+1)]
        x = 0
        for i, num in enumerate(arr):
            x ^= num
            preXOR[i] = x
        count = 0
        for i in range(n):
            for k in range(i+1, n):
                for j in range(i+1, k+1):
                    a = preXOR[i-1] ^ preXOR[j-1]
                    b = preXOR[j-1] ^ preXOR[k]
                    if a == b:
                        count += 1
        return count


# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preXOR = [0 for _ in range(n+1)]
        x = 0
        for i, num in enumerate(arr):
            x ^= num
            preXOR[i] = x
        count = 0
        for j in range(1, n):
            dic = {}
            for i in range(j):
                a = preXOR[j-1] ^ preXOR[i-1]
                dic[a] = dic.get(a, 0) + 1
            for k in range(j, n):
                b = preXOR[k] ^ preXOR[j-1]
                count += dic.get(b, 0)
        return count


# 3rd solution
# O(n^2) time | O(n) space
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preXOR = [0 for _ in range(n + 1)]
        x = 0
        for i, num in enumerate(arr):
            x ^= num
            preXOR[i] = x
        count = 0
        for k in range(n):
            for i in range(k):
                if preXOR[k] == preXOR[i-1]:
                    count += k - i
        return count


# 4th solution
# O(n) time | O(n) space
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        val = 0
        count = 0
        dic = {0: [0, 1]}
        
        for i, num in enumerate(arr):
            val ^= num
            if val not in dic:
                dic[val] = [i + 1, 1]
            else:
                count += dic[val][1] * i - dic[val][0]
                dic[val][0] += i + 1
                dic[val][1] += 1
        
        return count
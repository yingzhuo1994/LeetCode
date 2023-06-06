# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a1 = min(arr)
        an = max(arr)
        total = sum(arr)
        n = len(arr)
        if (a1 + an) * n != total * 2:
            return False
        diff = an - a1
        if diff % (n - 1) != 0:
            return False
        d = diff // (n - 1)

        if d == 0:
            return True

        mark = pow(10, 7)
        for i, num in enumerate(arr):
            if abs(num) > pow(10, 6):
                value = num - mark
            else:
                value = num
            idx, r = divmod(value - a1, d)
            if r != 0:
                return False
            if abs(arr[idx]) > pow(10, 6):
                return False
            arr[idx] += mark
        return True

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a1 = min(arr)
        an = max(arr)
        total = sum(arr)
        n = len(arr)
        if (a1 + an) * n != total * 2:
            return False
        diff = an - a1
        if diff % (n - 1) != 0:
            return False
        d = diff // (n - 1)

        if d == 0:
            return True

        i = 0
        while i < len(arr):
            if arr[i] == a1 + i * d:
                i += 1
            else:
                dis = arr[i] - a1
                if dis % d != 0:
                    return False
                pos = dis // d
                if arr[pos] == arr[i]:
                    return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True
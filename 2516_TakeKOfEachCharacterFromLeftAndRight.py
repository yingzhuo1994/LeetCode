# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        a_list = [0] * (n + 1)
        b_list = [0] * (n + 1)
        c_list = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == "a":
                a_list[i] += 1
            elif ch =="b":
                b_list[i] += 1
            else:
                c_list[i] += 1
            a_list[i] += a_list[i - 1]
            b_list[i] += b_list[i - 1]
            c_list[i] += c_list[i - 1]
        
        if a_list[n - 1] < k or b_list[n - 1] < k or c_list[n - 1] < k:
            return -1
        
        start = 1
        end = n
        length = 0
        while start <= end:
            mid = start + (end - start) // 2
            valid = False
            for i in range(n - mid + 1):
                j = i + mid - 1
                a = a_list[n - 1] - a_list[j] + a_list[i - 1]
                b = b_list[n - 1] - b_list[j] + b_list[i - 1]
                c = c_list[n - 1] - c_list[j] + c_list[i - 1]
                if a >= k and b >= k and c >= k:
                    valid = True
                    break
            if valid:
                length = max(length, mid)
                start = mid + 1
            else:
                end = mid - 1
        return n - length

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        n = len(s)
        a_dict = {0: -1}
        b_dict = {0: -1}
        c_dict = {0: -1}

        a = b = c = 0

        for i, ch in enumerate(s):
            if ch == "a":
                a += 1
            elif ch =="b":
                b += 1
            else:
                c += 1
            if a not in a_dict:
                a_dict[a] = i
            if b not in b_dict:
                b_dict[b] = i
            if c not in c_dict:
                c_dict[c] = i
        if a < k or b < k or c < k:
            return -1

        a_target = a - k
        b_target = b - k
        c_target = c - k

        a = b = c = 0
        x = y = z = -1
        length = 0
        for i, ch in enumerate(s):
            if ch == "a":
                a += 1
                x = a_dict.get(a - a_target, -1)
            elif ch =="b":
                b += 1
                y = b_dict.get(b - b_target, -1)
            else:
                c += 1
                z = c_dict.get(c - c_target, -1)
            length = max(length, i - max(x, y, z))
        return n - length

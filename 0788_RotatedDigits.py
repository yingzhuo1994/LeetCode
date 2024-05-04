# 1st solution
# O(n) time | O(1) space
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n + 1):
            s = str(num)
            if "3" in s or "4" in s or "7" in s:
                continue
            if "2" in s or "5" in s or "6" in s or "9" in s:
                count += 1
        return count


# 2nd soluton
# O(mD) time | O(m) space
# where m = log(n), D = 10
class Solution:
    def rotatedDigits(self, n: int) -> int:
        DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)
        s = str(n)
        @cache
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff  # 只有包含 2/5/6/9 才算一个好数
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(0, up + 1):  # 枚举要填入的数字 d
                if DIFFS[d] != -1:  # d 不是 3/4/7
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)
            return res
        return f(0, False, True)
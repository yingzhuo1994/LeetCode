# 1st solution
# O(a + b + c) time | O(a + b + c) space
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        order = [[a, "a"], [b, "b"], [c, "c"]]
        order.sort(reverse=True)
        a, ch_a = order[0]
        b, ch_b = order[1]
        c, ch_c = order[2]
        lst = []
        if a >= 2 * (b + c + 1):
            for _ in range(b):
                lst.append(ch_a * 2 + ch_b)
            for _ in range(c):
                lst.append(ch_a * 2 + ch_c)
            lst.append(ch_a * 2)
        else:
            r = a - b - c
            if r >= 0:
                for _ in range(b):
                    lst.append(ch_a + ch_b)
                for _ in range(c):
                    lst.append(ch_a + ch_c)
                for i in range(len(lst)):
                    if r == 0:
                        break
                    else:
                        lst[i] = ch_a + lst[i]
                        r -= 1
                if r > 0:
                    lst.append(ch_a * r)
            else:
                lst = [ch_a] * a
                for i in range(b):
                    lst[i] = lst[i] + ch_b
                for i in range(1, c + 1):
                    lst[-i] = ch_c + lst[-i]
        return "".join(lst)


# 2nd solution
# O(a + b + c) time | O(a + b + c) space
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                hasNext = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ans)
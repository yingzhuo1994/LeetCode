class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        m = len(bin(num1)) - 2
        n = len(bin(num2)) - 2
        cnt1 = Counter(bin(num1)[2:])
        cnt2 = Counter(bin(num2)[2:])
        if cnt2["1"] >= m:
            return (1 << cnt2["1"]) - 1
        ans = num1
        if cnt2["1"] >= cnt1["1"]:
            k = cnt2["1"] - cnt1["1"]
            d = 0
            while k > 0:
                if not ((ans >> d) & 1):
                    ans |= 1 << d
                    k -= 1
                d += 1
        else:
            k = cnt2["1"]
            d = m - 1
            while d >= 0:
                print(d, bin(ans >> d), (ans >> d) & 1)
                if (ans >> d) & 1:
                    if k <= 0:
                        ans ^= 1 << d
                    else:
                        k -= 1
                d -= 1
        return ans
# 1st solution
# O(n) time | O(1) space
class Solution:
    def compress(self, chars: List[str]) -> int:
        last = ""
        count = 0
        dic = {1, 9, 99, 999}
        length = 0
        idx = 0
        for ch in chars:
            if ch == last:
                if count in dic:
                    length += 1
                count += 1
            else:
                if count > 1:
                    for k in str(count):
                        chars[idx] = k
                        idx += 1
                chars[idx] = ch
                idx += 1
                last = ch
                count = 1
                length += 1
        if count > 1:
            for k in str(count):
                chars[idx] = k
                idx += 1
        chars[length:] = []

        return length
# 1st solution
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = 0
        A = []
        B = []
        for a, b in zip(s, goal):
            if a != b:
                diff += 1
                A.append(a)
                B.append(b)
            if diff > 2:
                return False
        if diff == 0:
            count = Counter(s)
            for ch in count:
                if count[ch] >= 2:
                    return True
        elif diff == 2:
            A.sort()
            B.sort()
            return A == B
        else:
            return False
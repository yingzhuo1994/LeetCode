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

# 2nd solution
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(goal):
            return True
        diff = [[a, b] for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0] == diff[1][::-1]
# 1st solution, TLE
# O(n1 * len(s1)) time | O(1) space
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        count_s1 = Counter(s1)
        count_s2 = Counter(s2)

        for ch in count_s2:
            if ch not in count_s1:
                return 0
        new_s1 = []
        for ch in s1:
            if ch not in count_s2:
                continue
            new_s1.append(ch)
        s1 = "".join(new_s1)
        index = 0
        repeat_count = 0
        s1_size = len(s1)
        s2_size = len(s2)
        for _ in range(n1):
            for j in range(s1_size):
                if s1[j] == s2[index]:
                    index += 1
                if index == s2_size:
                    index = 0
                    repeat_count += 1

        return repeat_count // n2

# 2nd solution
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        start = {} # s2_idx : s1_round, s2_round
        s1_round, s2_round, s2_idx = 0, 0, 0
        while s1_round < n1:
            s1_round += 1
            for ch in s1:
                if ch == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_round += 1
                        s2_idx = 0
            if s2_idx in start:
                prev_s1_round, prev_s2_round = start[s2_idx]
                circle_s1_round, circle_s2_round = s1_round - prev_s1_round, s2_round - prev_s2_round
                res = (n1 - prev_s1_round) // circle_s1_round * circle_s2_round
                left_s1_round = (n1 - prev_s1_round) % circle_s1_round + prev_s1_round
                for key, val in start.items():
                    if val[0] == left_s1_round:
                        res += val[1]
                        break
                return res // n2
            else:
                start[s2_idx] = (s1_round, s2_round)
        return s2_round // n2
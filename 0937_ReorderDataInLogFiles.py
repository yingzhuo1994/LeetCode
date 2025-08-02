# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            lst = log.split()
            if all(ch.isdigit() for ch in lst[1:]):
                digit_logs.append(log)
            else:
                letter_logs.append(lst)
        letter_logs.sort(key=lambda v: [v[1:], -len(v), v[0:1]])
        letter_logs = [" ".join(log) for log in letter_logs]
        return letter_logs + digit_logs
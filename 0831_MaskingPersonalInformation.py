# 1st solution
# O(n) time | O(n) space
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            email = name[0] + "*****" + name[-1] + "@" + domain
            return email
        else:
            number = s.translate(str.maketrans('', '', "+-() "))
            if len(number) == 10:
                return "***-***-" + number[-4:]
            else:
                k = len(number) - 10
                code = "*" * k
                return "+" + code + "-***-***-" + number[-4:]
# 1st solution
# O(n) time | O(n) space
class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            email = name[0].lower() + "*****" + name[-1].lower() + "@" + domain.lower()
            return email
        else:
            number = s.translate(str.maketrans('', '', "+-() "))
            if len(number) == 10:
                return "***-***-" + number[-4:]
            else:
                k = len(number) - 10
                code = "*" * k
                return "+" + code + "-***-***-" + number[-4:]
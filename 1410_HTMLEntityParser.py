# 1st solution
# O(n) time | O(n) space
class Solution:
    def entityParser(self, text: str) -> str:
        dic = {"&quot;": '"', "&apos;": "'", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        s = text
        for k, v in dic.items():
            s = s.replace(k, v)
        s = s.replace("&amp;", "&")
        return s
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if s and p[0] in {s[0], '.'}:
            first_match = True
        else:
            first_match = False
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
                
            
            

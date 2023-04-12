# 1st solution
# O(n) time | O(n) space
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = filter(self.isImportantCharacter, path.split("/"))
        ans = [""]
        for ch in stack:
            if ch == "..":
                if ans[-1] != "":
                    ans.pop()
            else:
                ans.append(ch)
        if len(ans) == 1 and ans[0] == "":
            return "/"
        return "/".join(ans)
    
    def isImportantCharacter(self, ch):
        return len(ch) > 0 and ch != "."

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for ch in path:
            if ch == "" or ch == ".":
                continue
            elif ch == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/" + "/".join(stack)

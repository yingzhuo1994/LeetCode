# O(n) time | O(n) space
# where n is the number of files
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_file = defaultdict(list)

        for path in paths:
            stack = path.split(" ")
            curPath = stack[0]
            for i in range(1, len(stack)):
                file = stack[i]
                newStack = file.split("(")
                fileName= newStack[0]
                fileContent = newStack[1][:-1]
                content_to_file[fileContent].append(curPath + "/" + fileName)
        
        ans = []
        for fileContent in content_to_file:
            if len(content_to_file[fileContent]) >= 2:
                ans.append(content_to_file[fileContent])
        return ans
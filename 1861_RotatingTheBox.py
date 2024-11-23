# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for row in box:
            last = n
            for j in reversed(range(n)):
                if row[j] == "*":
                    last = j
                elif row[j] == "#":
                    row[j] = "."
                    row[last - 1] = "#"
                    last -= 1
        box_t = [[box[i][j] for i in reversed(range(m))] for j in range(n)]
        return box_t
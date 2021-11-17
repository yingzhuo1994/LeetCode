# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        nodes = collections.defaultdict(list)
        queue = deque([(root,0,0)])
        findX = False
        findY = False
        while queue:
            node,level,parent = queue.popleft()
            nodes[node.val] = [level,parent]
            if node.val == x:
                findX = True
            if node.val == y:
                findY = True
            if findX and findY:
                break
            if node.left:
                queue.append((node.left,level+1,node.val))
            if node.right:
                queue.append((node.right,level+1,node.val))

        if nodes[x][0] == nodes[y][0] and nodes[x][1] != nodes[y][1]:
            return True

        return False

# 2nd solution
# O(n) time | O(log(n)) space
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = None
        self.y = None
        self.findParent(root, x, y, 0, None)
        return self.x[0] == self.y[0] and self.x[1] != self.y[1]

    def findParent(self, node, x, y, depth, parent):
        if not node:
            return 
        if self.x and self.y:
            return
        if node.val == x:
            self.x =  [depth, parent]
        if node.val == y:
            self.y = [depth, parent]
        self.findParent(node.left, x, y, depth + 1, node)
        self.findParent(node.right, x, y, depth + 1, node)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = defaultdict(list)
        isAdded = set()
        ans = []
        def getDepth(node, depth=0):
            if not node:
                return 0
            return max(getDepth(node.left), getDepth(node.right)) + 1

        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        def hasSameTree(node):
            findSame = False
            depth = getDepth(node)
            for curNode in dic[(node.val, depth)]:
                if isSameTree(curNode, node):
                    return curNode

                if findSame:
                    break
            if not findSame:
                dic[(node.val, depth)].append(node)
            return None
        
        def appendNode(node):
            if not node:
                return
            if node not in isAdded:
                ans.append(node)
                isAdded.add(node)
                # appendNode(node.left)
                # appendNode(node.right)
        
        def dfs(node):
            if not node:
                return
            oldNode =  hasSameTree(node)
            if oldNode is not None:
                appendNode(oldNode)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def trv(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
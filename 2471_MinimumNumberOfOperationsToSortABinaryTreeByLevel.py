# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def compare(lst):
            ordered = sorted(lst[:])
            dic = {num: i for i, num in enumerate(lst)}
            count = 0
            for i in range(len(lst)):
                if lst[i] != ordered[i]:
                    j = dic[ordered[i]]
                    dic[lst[i]] = j
                    dic[ordered[i]] = i
                    lst[i], lst[j] = lst[j], lst[i]
                    count += 1
            return count

        level = [root]
        ans = 0
        while level:
            values = [node.val for node in level]
            ans += compare(values)
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel
        return ans
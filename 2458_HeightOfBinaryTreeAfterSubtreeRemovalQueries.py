# 1st solution
# O(n) time | O(n) space
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)  # 每棵子树的高度
        def get_height(node: Optional[TreeNode]) -> int:
            if node is None: return 0
            height[node] = 1 + max(get_height(node.left), get_height(node.right))
            return height[node]
        get_height(root)

        res = [0] * (len(height) + 1)  # 每个节点的答案
        def dfs(node: Optional[TreeNode], depth: int, rest_h: int) -> None:
            if node is None: return
            depth += 1
            res[node.val] = rest_h
            dfs(node.left, depth, max(rest_h, depth + height[node.right]))
            dfs(node.right, depth, max(rest_h, depth + height[node.left]))
        dfs(root, -1, 0)

        for i, q in enumerate(queries):
            queries[i] = res[q]
        return queries
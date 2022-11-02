# 1st solution, BFS
# O(4^n) time | O(4^n) space
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if start == end:
            return 0
        if end not in bank:
            return -1
        
        stack = deque([[start, 0]])
        visited = set([start])
        while stack:
            gene, step = stack.popleft()
            for i in range(len(gene)):
                for ch in "ACGT":
                    new_gene = gene[:i] + ch + gene[i+1:]
                    if new_gene == end:
                        return step + 1
                    if new_gene not in visited and new_gene in bank:
                        visited.add(new_gene)
                        stack.append([new_gene, step + 1])
        return -1
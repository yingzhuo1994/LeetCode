# 1st solution
# O(n) time | O(n) space
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        n = len(pairs)
        if n == 1:
            return pairs
        graph = {}
        graph_rev = {}
        cnt = {}
        for a, b in pairs:
            cnt[a] = cnt.get(a, 0) - 1
            cnt[b] = cnt.get(b, 0) + 1
            if a not in graph:
                graph[a] = deque()
            graph[a].append(b)
            if b not in graph_rev:
                graph_rev[b] = deque()
            graph_rev[b] = a
        
        src = None
        sink = None
        for a in cnt:
            if cnt[a] < 0:
                src = a
            elif cnt[b] > 0:
                sink = b
        
        order = True
        if src is None and sink is None:
            stack = [pairs[0][0]]
        elif src is not None:
            stack = [src]
        elif sink is not None:
            stack = [sink]
        
        if order:
            dic = graph
        else:
            dic = graph_rev

        back = []
        while len(dic) > 0:
            last = stack[-1]
            if last in dic:
                ch = dic[last].popleft()
                stack.append(ch)
                if len(dic[last]) == 0:
                    del dic[last]
            else:
                back.append(stack.pop())

        stack.extend(back[::-1])
        if order:
            ans = [[stack[i], stack[i + 1]] for i in range(len(stack) - 1)]
        else:
            ans = [[stack[i + 1], stack[i]] for i in reversed(range(len(stack) - 1))]
        return ans
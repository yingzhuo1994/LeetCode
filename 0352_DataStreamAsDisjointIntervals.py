# 1st solution
class SummaryRanges:
    def __init__(self):
        self.ds = DisjointSet()
        
    def addNum(self, value: int) -> None:
        self.ds.add(value)
        
    def getIntervals(self) -> List[List[int]]:
        return self.ds.head.getIntervals()

class DisjointSet:
    def __init__(self):
        self.head = DLinkedList()
        self.parents = {-2: -2}
        self.nodes = {-2: self.head.sentinel}
        self.endVals = {-2: self.head.sentinel}
        
    def add(self, num):
        if num in self.parents:
            return
        self.parents[num] = num
        node = Node(num, num)
        self.nodes[num] = node
        self.endVals[num] = node

        values = sorted(self.endVals.keys())
        idx = bisect.bisect_left(values, num) - 1
        key = values[idx]
        prevNode = self.nodes[self.getParent(key)]
        self.head.appendAfter(prevNode, node)
        nextNode = node.next

        if prevNode.end == num - 1:
            prevNode.end = num
            self.parents[num] = prevNode.start
            self.head.pop(node)
            self.endVals.pop(num - 1)
            self.endVals[num] = prevNode
        
        if nextNode.start == num + 1:
            nextNode.prev.end = nextNode.end
            self.parents[nextNode.start] = nextNode.prev.start
            self.head.pop(nextNode)
            self.endVals.pop(num)
            self.endVals[nextNode.end] = nextNode.prev

    def getParent(self, num):
        pa = self.parents[num]
        if pa != num:
            self.parents[num] = self.getParent(pa)
        return self.parents[num]

class Node:
    def __init__(self, start=-2, end=-2):
        self.start = start
        self.end = end
        self.prev = None
        self.next = None
    
    def getSize(self):
        return self.end - self.start + 1

class DLinkedList:
    def __init__(self):
        self.sentinel = Node()
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
    
    def appendAfter(self, curNode, newNode):
        newNode.prev = curNode
        newNode.next = curNode.next
        curNode.next = newNode
        newNode.next.prev = newNode
    
    def appendBefore(self, curNode, newNode):
        self.appendAfter(curNode.prev, newNode)
    
    def pop(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def getIntervals(self):
        intervals = []
        node = self.sentinel.next
        while node != self.sentinel:
            intervals.append([node.start, node.end])
            node = node.next
        return intervals

# 2nd solution, Heap method
from heapq import heappush, heappop
class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heappush(self.intervals, (val, [val, val]))

    def getIntervals(self):
        stack = []
        while self.intervals:
            idx, cur = heappop(self.intervals)
            if not stack:
                stack.append((idx, cur))
            else:
                _, prev = stack[-1]
                if prev[1] + 1 >= cur[0]:
                    prev[1] = max(prev[1], cur[1])
                else:
                    stack.append((idx, cur))
        self.intervals = stack
        return list(map(lambda x: x[1], stack))

# 3rs solution, Disjoint Set
class DSU:
    def __init__(self):
        self.parents = {}
        self.intervals = {}

    def exists(self, x): 
        return x in self.parents

    def make_set(self, x):
        self.parents[x] = x
        self.intervals[x] = [x, x]
        
    def getParent(self, x):
        if not self.exists(x): return None
        
        if self.parents[x] != x:
            self.parents[x] = self.getParent(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        xr = self.getParent(x)
        yr = self.getParent(y)
        
        if xr is None or yr is None: return
        
        self.parents[xr] = yr
        
        ## interval adjusting logic
        x_interval = self.intervals[xr]
        del self.intervals[xr]
        
        self.intervals[yr] = [min(self.intervals[yr][0], x_interval[0]), max(self.intervals[yr][1], x_interval[1])]
        
class SummaryRanges:    
    def __init__(self):
        self.dsu = DSU()

    def addNum(self, val: int) -> None:
        if self.dsu.exists(val): return
            
        self.dsu.make_set(val)
        
        self.dsu.union(val, val-1)
        self.dsu.union(val, val+1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.dsu.intervals.values())

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
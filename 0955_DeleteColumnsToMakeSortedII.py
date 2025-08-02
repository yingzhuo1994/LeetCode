# 1st solution
# O(n) time | O(n) space
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def compare(a, b):
            s_set = set()
            for i in range(len(a)):
                if i in del_set:
                    continue
                if a[i] < b[i]:
                    break
                elif a[i] > b[i]:
                    s_set.add(i)
            return s_set
        
        del_set = set()

        mark = 1
        while mark:
            mark = 0
            for i in range(len(strs) - 1):
                s_set = compare(strs[i], strs[i + 1])
                if s_set:
                    mark = 1
                del_set |= s_set
            
        return len(del_set)
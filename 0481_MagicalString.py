# O(n) time | O(n) space
class Solution:
    def magicalString(self, n: int) -> int:
        lst = [1]
        i = 0
        j = 0
        while len(lst) < n:
            if lst[i] == 1:
                if lst[j] == 1:
                    lst.append(2)
                else:
                    lst.append(1)
                j += 1
            else:
                if lst[j] == 1:
                    lst.extend([1, 2])
                else:
                    lst.extend([2, 1])
                j += 2
            i += 1
            print(lst)
        count = Counter(lst[:n])
        return count[1]
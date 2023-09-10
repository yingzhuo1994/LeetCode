# 1st solution
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        bulbs = [1 for _ in range(n)]
        bulbs = tuple(bulbs)

        dic = {0: set([bulbs])}
        for k in range(1, presses + 1):
            last = dic[k - 1]

            new = set()
            for button in range(1, 5):
                if button == 1:
                    for key in last:
                        lst = list(key)
                        lst = [-1 * s for s in lst]
                        newKey = tuple(lst)
                        new.add(newKey)
                elif button == 2:
                    for key in last:
                        lst = list(key)
                        lst = [s if i & 1 else s * -1 for i, s in enumerate(lst)]
                        newKey = tuple(lst)
                        new.add(newKey)
                elif button == 3:
                    for key in last:
                        lst = list(key)
                        lst = [-1 * s if i & 1 else s for i, s in enumerate(lst)]
                        newKey = tuple(lst)
                        new.add(newKey)
                else:
                    for key in last:
                        lst = list(key)
                        lst = [-1 * s if (i + 1) % 3 == 1 else s for i, s in enumerate(lst)]
                        newKey = tuple(lst)
                        new.add(newKey)
            dic[k] = new

        return len(dic[presses])
                

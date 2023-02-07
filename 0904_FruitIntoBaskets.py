# 1st solution
# O(n) time | O(n) space
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count_lst = []
        n = len(fruits)

        start = 0
        i = 0
        while i <= n:
            if i == n or fruits[i] != fruits[start]:
                count_lst.append([fruits[start], i - start])
                start = i
            i += 1
        
        if len(count_lst) == 1:
            return count_lst[0][1]
        elif len(count_lst) == 2:
            return count_lst[0][1] + count_lst[1][1]
        ans = count_lst[0][1] + count_lst[1][1]
        cur_fruits = {count_lst[0][0]: [count_lst[0][1], 0], count_lst[1][0]: [count_lst[1][1], 1]}

        for i in range(2, len(count_lst)):
            fruit, count = count_lst[i]
            if fruit in cur_fruits:
                cur_fruits[fruit][0] += count
                cur_fruits[fruit][1] = i
            else:
                lst = list(cur_fruits.keys())
                for key in lst:
                    if cur_fruits[key][1] != i - 1:
                        cur_fruits.pop(key)
                    else:
                        cur_fruits[key][0] = count_lst[cur_fruits[key][-1]][1]
                cur_fruits[fruit] = [count, i]

            curSum = 0
            for key in cur_fruits:
                curSum += cur_fruits[key][0]
            ans = max(ans, curSum)

        return ans


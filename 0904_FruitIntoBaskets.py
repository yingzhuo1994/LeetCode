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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
       
        ans = 1
        cur_fruits = {fruits[0]: [1, 1, 0]}

        for i in range(1, n):
            fruit = fruits[i]
            if fruit in cur_fruits:
                cur_fruits[fruit][0] += 1
                if cur_fruits[fruit][2] == i - 1:
                    cur_fruits[fruit][1] += 1
                else:
                    cur_fruits[fruit][1] = 1
                cur_fruits[fruit][2] = i
            else:
                if len(cur_fruits) == 2:
                    lst = list(cur_fruits.keys())
                    for key in lst:
                        if cur_fruits[key][2] != i - 1:
                            cur_fruits.pop(key)
                        else:
                            cur_fruits[key][0] = cur_fruits[key][1]
                cur_fruits[fruit] = [1, 1, i]

            curSum = 0
            for key in cur_fruits:
                curSum += cur_fruits[key][0]
            ans = max(ans, curSum)

        return ans

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, nums, res = 0, collections.Counter(), 0
        for r in range(len(fruits)):
            nums[fruits[r]] += 1
            while len(nums) > 2:
                nums[fruits[l]] -= 1 
                if not nums[fruits[l]]:
                    nums.pop(fruits[l])
                l += 1
            res = max(res, r - l + 1)
        return res

# 4th solution
# O(n) time | O(1) space
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i = {}, 0
        for j, v in enumerate(fruits):
            count[v] = count.get(v, 0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0: del count[fruits[i]]
                # always keep the longest length
                i += 1
        return j - i + 1
# 1st solution
# O(n) time | O(1) space
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def count_element(s, i):
            dic = {}
            elem = ""
            num = 0
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch.isupper():
                    if elem != "":
                        dic[elem] = dic.get(elem, 0) + max(num, 1)
                    elem = ch
                    num = 0
                elif ch.islower():
                    elem += ch
                elif ch == "(":
                    if elem != "":
                        dic[elem] = dic.get(elem, 0) + max(num, 1)
                    elem = ""
                    lastDic, j = count_element(s, i + 1)
                    k = j
                    while k < len(s) and s[k].isdigit():
                        k += 1
                    num = 1
                    if k > j:
                        num = int(s[j:k])
                        print(num)
                    for key, value in lastDic.items():
                        if key not in dic:
                            dic[key] = value * num
                        else:
                            dic[key] += value * num
                    i = k - 1
                elif ch == ")":
                    if elem != "":
                        dic[elem] = dic.get(elem, 0) + max(num, 1)
                    return dic, i + 1
                i += 1
            if elem != "":
                dic[elem] = dic.get(elem, 0) + max(num, 1)
            return dic

        
        dic = count_element(formula, 0)
        keys = list(dic.keys())
        keys.sort()
        lst = []
        for key in keys:
            if dic[key] > 1:
                lst.append(key + str(dic[key]))
            else:
                lst.append(key)
        return "".join(lst)


# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        map = defaultdict(lambda: 1)
        d = deque([])
        i = idx = 0
        while i < n:
            c = formula[i]
            if c == '(' or c == ')':
                d.append(c)
                i += 1
            else:
                if str.isdigit(c):
                    # 获取完整的数字，并解析出对应的数值
                    j = i
                    while j < n and str.isdigit(formula[j]):
                        j += 1
                    cnt = int(formula[i:j])
                    i = j
                    # 如果栈顶元素是 )，说明当前数值可以应用给「连续一段」的原子中
                    if d and d[-1] == ')':
                        tmp = []
                        d.pop()
                        while d and d[-1] != '(':
                            cur = d.pop()
                            map[cur] *= cnt
                            tmp.append(cur)
                        d.pop()

                        for k in range(len(tmp) - 1, -1, -1):
                            d.append(tmp[k])
                    # 如果栈顶元素不是 )，说明当前数值只能应用给栈顶的原子
                    else:
                        cur = d.pop()
                        map[cur] *= cnt
                        d.append(cur)
                else:
                    # 获取完整的原子名
                    j = i + 1
                    while j < n and str.islower(formula[j]):
                        j += 1
                    cur = formula[i:j] + "_" + str(idx)
                    idx += 1
                    map[cur] = 1
                    i = j
                    d.append(cur)

        #  将不同编号的相同原子进行合并
        mm = defaultdict(int)
        for key, cnt in map.items():
            atom = key.split("_")[0]
            mm[atom] += cnt

        # 对mm中的key进行排序作为答案
        ans = []
        for key in sorted(mm.keys()):
            if mm[key] > 1:
                ans.append(key+str(mm[key]))
            else:
                ans.append(key)
        return "".join(ans)
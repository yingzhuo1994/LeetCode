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
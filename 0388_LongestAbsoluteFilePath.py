# 1st solution
# O(nd) time | O(n) space
# where n is string length, and d is the largerst file level.  
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dic = {}
        longest = 0
        fileList = input.split("\n")
        for i in fileList:
            key = i.count("\t") #是几级文件夹
            if "." not in i:  #是文件夹
                value = len(i) - key
                dic[key] = value
            else: #是文件。
                #　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
                length = sum([dic[j] for j in range(key)]) + len(i)
                longest = max(longest, length)
        return longest

# 2nd solution
# O(nd) time | O(n) space
# where n is string length, and d is the largerst file level.  
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dic = {-1: 0}
        longest = 0
        fileList = input.split("\n")
        for i in fileList:
            key = i.count("\t")
            if "." not in i: 
                value = len(i) - key
                dic[key] = dic[key-1] + value
            else:
                length = dic[key-1] + len(i)
                longest = max(longest, length)
        return longest
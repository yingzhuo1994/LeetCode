# 1st solution
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dict = {}
        longest = 0
        fileList = input.split("\n")
        for i in fileList:
            key = i.count("\t") #是几级文件夹
            if "." not in i:  #是文件夹
                value = len(i) - key
                dict[key] = value
            else: #是文件。
                #　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
                length = sum([dict[j] for j in range(key)]) + len(i)
                longest = max(longest, length)
        return longest